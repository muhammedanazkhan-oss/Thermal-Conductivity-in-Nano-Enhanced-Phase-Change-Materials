import warnings; warnings.filterwarnings("ignore")
import numpy as np, pandas as pd, json
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import KFold, cross_val_score, cross_val_predict
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
np.random.seed(42)
df=pd.read_csv("nepcm_databank.csv")
for c in ["keff_WmK","base_k_WmK","loading_wt","filler_k_WmK","temp_C"]: df[c]=pd.to_numeric(df[c],errors="coerce")
df=df[df["keff_WmK"].notna()&df["base_k_WmK"].notna()].copy(); df["temp_C"]=df["temp_C"].fillna(25)
df["logfk"]=np.log10(df["filler_k_WmK"]+1); df["phase_liquid"]=(df["phase"]=="liquid").astype(int)
FEATS=["loading_wt","logfk","temp_C","phase_liquid","hybrid_flag"]   # FIVE inputs (base_k is normaliser)
X=df[FEATS].values; y=np.log10(df["keff_WmK"]/df["base_k_WmK"]).values   # TARGET y = log10(keff/kbase)
def mk():
 return {"M1 Linear regression":make_pipeline(StandardScaler(),LinearRegression()),
  "M2 SVR (RBF)":make_pipeline(StandardScaler(),SVR(C=10,gamma="scale",epsilon=0.02)),
  "M3 Random forest":make_pipeline(StandardScaler(),RandomForestRegressor(n_estimators=200,max_depth=10,min_samples_leaf=2,random_state=42)),
  "M4 Gradient boosting":make_pipeline(StandardScaler(),GradientBoostingRegressor(n_estimators=200,max_depth=3,learning_rate=0.05,random_state=42)),
  "M5 Neural network":make_pipeline(StandardScaler(),MLPRegressor(hidden_layer_sizes=(24,12),activation="tanh",alpha=1e-3,solver="lbfgs",max_iter=500,random_state=42))}
cv=KFold(10,shuffle=True,random_state=42); order=list(mk()); res={}
print("N=%d  |  target y=log10(keff/kbase)  |  %d features"%(len(df),len(FEATS)))
print("%-22s %14s %10s %8s %8s %10s"%("Model","CV R2(y)","RMSE(y)","MAE(y)","trainR2","gap"))
for n in order:
 r2=cross_val_score(mk()[n],X,y,cv=cv,scoring="r2")
 rmse=-cross_val_score(mk()[n],X,y,cv=cv,scoring="neg_root_mean_squared_error")
 mae=-cross_val_score(mk()[n],X,y,cv=cv,scoring="neg_mean_absolute_error")
 m=mk()[n]; m.fit(X,y); tr=r2_score(y,m.predict(X))
 res[n]={"cv_r2":float(r2.mean()),"cv_r2_sd":float(r2.std()),"cv_rmse":float(rmse.mean()),"cv_rmse_sd":float(rmse.std()),
         "cv_mae":float(mae.mean()),"cv_mae_sd":float(mae.std()),"train_r2":float(tr)}
 print("%-22s %6.2f (± %.2f) %8.3f %8.3f %8.2f %8.2f"%(n,r2.mean(),r2.std(),rmse.mean(),mae.mean(),tr,tr-r2.mean()))
best=max(res,key=lambda k:res[k]["cv_r2"])
# LOSO on y
srcs=df["source"].values; yhat=np.full(len(y),np.nan)
for s in np.unique(srcs):
    tr_=srcs!=s
    if tr_.sum()<10: continue
    mm=mk()[best].fit(X[tr_],y[tr_]); yhat[~tr_]=mm.predict(X[~tr_])
ok=~np.isnan(yhat); loso=r2_score(y[ok],yhat[ok])
print("\nBest by CV R2(y): %s  |  LOSO R2(y)=%.2f"%(best,loso))
json.dump({"n":int(len(df)),"features":FEATS,"target":"log10(keff/kbase)","best":best,"loso_r2":float(loso),"results":res},open("model_results_y.json","w"),indent=2)
# OOF for parity
oof=cross_val_predict(mk()[best],X,y,cv=cv); df.assign(y_true=y,y_oof=oof,loso=np.where(ok,yhat,np.nan)).to_csv("oof_y.csv",index=False)
print("saved model_results_y.json, oof_y.csv")
