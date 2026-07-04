import csv
FK={"EG":100,"MWCNT":3000,"CNF":2000,"graphene":4000,"GNP":4000,"GO":100,"rGO":1500,
"Al2O3":35,"SiO2":1.4,"TiO2":8.5,"CuO":33,"ZnO":25,"Fe2O3":7,"CeO2":10,"SiC":120,"Ag":429,"Cu":400,"BN":300,"cBN":750}
rows=[]
def add(src,pcm,fil,cls,hyb,load,fk,pc,T,phase,bk,keff,ks="EXACT",wf=""):
    dk = round((keff-bk)/bk*100,1) if (bk and keff) else ""
    rows.append(dict(source=src,base_pcm=pcm,filler=fil,filler_class=cls,hybrid_flag=hyb,loading_wt=load,
        filler_k_WmK=fk,particle_size_nm=pc,temp_C=T,phase=phase,base_k_WmK=bk,keff_WmK=keff,delta_k_pct=dk,keff_source=ks,where=wf))

# 1 Sari & Karaipekli 2007 (paraffin/EG)
for L,k in [(0,0.22),(2,0.40),(4,0.52),(7,0.68),(10,0.82)]:
    add("Sari & Karaipekli 2007","paraffin",("none" if L==0 else "EG"),("base" if L==0 else "carbon"),0,L,(0 if L==0 else 100),"NR",25,"solid",0.22,k,wf="text p.1274")
# 2 Motahar 2016 (n-octadecane/MWCNT,CNF)
for L,T,k in [(0.5,5,0.414),(1,5,0.448),(2,5,0.445),(5,5,0.510),(0.5,20,0.400),(1,20,0.429),(2,20,0.450),(5,20,0.480)]:
    add("Motahar 2016","n-octadecane","MWCNT","carbon",0,L,3000,140,T,"solid",0.375,k,"EXACT","Fig2a text")
add("Motahar 2016","n-octadecane","MWCNT","carbon",0,5,3000,140,30,"liquid",0.165,0.229,"EXACT","Fig2b text")
for L,T,k in [(0.5,30,0.167),(1,30,0.180),(2,30,0.185),(5,30,0.189),(0.5,55,0.154),(1,55,0.165),(2,55,0.170),(5,55,0.175)]:
    add("Motahar 2016","n-octadecane","CNF","carbon",0,L,2000,137,T,"liquid",0.165,k,"EXACT","Fig4b text")
# 3 Sharma 2025 (beeswax/SiO2-CeO2 hybrid)
add("Sharma 2025","beeswax","none","base",0,0,0,"NR",25,"solid",0.24,0.24,"EXACT","abstract")
add("Sharma 2025","beeswax","SiO2-CeO2","hybrid",1,1.0,5.7,"NR",25,"solid",0.24,0.40,"EXACT","abstract")
add("Sharma 2025","beeswax","SiO2-CeO2","hybrid",1,2.0,5.7,"NR",25,"solid",0.24,0.42,"COMPUTED","abstract 75%")
# 4 Harish 2015 (lauric acid/graphene) 1vol%=2.5wt%
add("Harish 2015","lauric acid","none","base",0,0,0,"NR",20,"solid",0.215,0.215,"EXACT","text")
add("Harish 2015","lauric acid","graphene","carbon",0,2.5,4000,7,20,"solid",0.215,0.489,"EXACT","text")
# 5 Manoj Kumar 2019 (paraffin/SiO2)
for L,k in [(0,0.180),(0.5,0.203),(1,0.221),(2,0.240)]:
    add("Manoj Kumar 2019","paraffin",("none" if L==0 else "SiO2"),("base" if L==0 else "oxide"),0,L,(0 if L==0 else 1.4),15,25,"solid",0.180,k,"EXACT","text")
# 6 Maher 2021 (paraffin/SiC,Ag) computed from %
add("Maher 2021","paraffin","SiC","carbide",0,15,120,80,25,"solid",0.25,0.396,"COMPUTED","abstract 58.2%")
add("Maher 2021","paraffin","Ag","metal",0,15,429,80,25,"solid",0.25,0.328,"COMPUTED","abstract 31.2%")
# 7 Nourani 2016 (paraffin/Al2O3) solid+liquid
add("Nourani 2016","paraffin","none","base",0,0,0,15,25,"solid",0.197,0.197,"EXACT","Table6")
add("Nourani 2016","paraffin","none","base",0,0,0,15,60,"liquid",0.148,0.148,"EXACT","Table6")
for L,k in [(2.5,0.227),(5,0.236),(7.5,0.245),(10,0.259)]:
    add("Nourani 2016","paraffin","Al2O3","oxide",0,L,35,15,25,"solid",0.197,k,"EXACT","Table6")
for L,k in [(2.5,0.152),(5,0.156),(7.5,0.162),(10,0.167)]:
    add("Nourani 2016","paraffin","Al2O3","oxide",0,L,35,15,60,"liquid",0.148,k,"EXACT","Table6")
# 8 Xia 2010 (paraffin/EG)
add("Xia 2010","paraffin","none","base",0,0,0,"NR",15,"solid",0.305,0.305,"EXACT","Table1")
add("Xia 2010","paraffin","EG","carbon",0,10,100,"NR",15,"solid",0.305,3.83,"EXACT","text")
# 9 Qu 2019 (octadecane-HDPE/hybrid) all 5wt%
add("Qu 2019","octadecane-HDPE","EG","carbon",0,5,100,"NR",25,"solid",0.25,0.85,"EXACT","Sec3.1")
add("Qu 2019","octadecane-HDPE","MWCNT","carbon",0,5,3000,"NR",25,"solid",0.25,0.52,"EXACT","Sec3.1")
add("Qu 2019","octadecane-HDPE","CNF","carbon",0,5,2000,"NR",25,"solid",0.25,0.37,"EXACT","Sec3.1")
add("Qu 2019","octadecane-HDPE","EG-MWCNT 4:1","hybrid",1,5,1550,"NR",25,"solid",0.25,1.36,"EXACT","Table4")
add("Qu 2019","octadecane-HDPE","EG-MWCNT 3:2","hybrid",1,5,1550,"NR",25,"solid",0.25,1.09,"EXACT","Table4")
add("Qu 2019","octadecane-HDPE","EG-CNF 4:1","hybrid",1,5,1050,"NR",25,"solid",0.25,1.03,"EXACT","Table4")
# 10 Arshad 2020 (RT-35HC) 1wt%, solid20 + phase-change35
for fil,cls,fk,hy,k20,k35 in [("GO","carbon",100,0,0.374,0.957),("rGO","carbon",1500,0,0.373,0.935),("GNP","carbon",4000,0,0.378,0.966),("MWCNT","carbon",3000,0,0.354,0.921),("GO-MWCNT","hybrid",1550,1,0.408,0.961),("rGO-MWCNT","hybrid",2250,1,0.428,0.965),("GNP-MWCNT","hybrid",3500,1,0.443,0.970)]:
    add("Arshad 2020","RT-35HC",fil,cls,hy,1,fk,"NR",20,"solid",0.214,k20,"EXACT","Sec3.6")
    add("Arshad 2020","RT-35HC",fil,cls,hy,1,fk,"NR",35,"liquid",0.340,k35,"EXACT","Sec3.6")
# 11 Li 2019 (paraffin/EG,GO,GR)
add("Li 2019","paraffin","none","base",0,0,0,"NR",25,"solid",0.201,0.201,"EXACT","Table2")
for fil,cls,fk,vals in [("EG","carbon",100,[(0.5,0.224),(1,0.239),(1.5,0.252),(2,0.272)]),("GO","carbon",100,[(0.5,0.244),(1,0.266),(1.5,0.286),(2,0.309)]),("graphene","carbon",4000,[(0.5,0.266),(1,0.289),(1.5,0.312),(2,0.348)])]:
    for L,k in vals: add("Li 2019","paraffin",fil,cls,0,L,fk,"NR",25,"solid",0.201,k,"EXACT","Table2")
# 12 He 2018 (PEG/GNP)
add("He 2018","PEG","none","base",0,0,0,2,25,"solid",0.316,0.316,"EXACT","text")
add("He 2018","PEG","GNP","carbon",0,2,4000,2,25,"solid",0.316,0.776,"EXACT","text")
# 13 Paprota 2024 (fatty-acid/BN)
add("Paprota 2024","stearic acid blend","none","base",0,0,0,500,25,"solid",0.252,0.252,"EXACT","Table9")
for L,k in [(0.5,0.284),(1,0.313),(2,0.306),(5,0.324)]:
    add("Paprota 2024","stearic acid blend","h-BN","nitride",0,L,300,500,25,"solid",0.252,k,"EXACT","Table9")
for L,k in [(0.5,0.324),(1,0.297),(2,0.274),(5,0.326)]:
    add("Paprota 2024","stearic acid blend","c-BN","nitride",0,L,750,165,25,"solid",0.252,k,"EXACT","Table9")
# 14 Huang 2023 (SA-BA eutectic/BN,EG,BN+EG)
add("Huang 2023","stearic acid-benzamide","none","base",0,0,0,"NR",25,"solid",0.3393,0.3393,"EXACT","Sec3.6")
for L,k in [(10,0.5878),(15,0.7278),(20,0.9647)]: add("Huang 2023","stearic acid-benzamide","BN","nitride",0,L,300,100,25,"solid",0.3393,k,"EXACT","Sec3.6")
for L,k in [(10,3.525),(15,4.913),(20,6.377)]: add("Huang 2023","stearic acid-benzamide","EG","carbon",0,L,100,"NR",25,"solid",0.3393,k,"EXACT","Sec3.6")
for L,k in [(20,3.805),(25,3.977),(30,4.184),(25,5.278),(30,5.486),(35,5.552),(30,6.791),(35,6.990),(40,7.097)]:
    add("Huang 2023","stearic acid-benzamide","BN-EG","hybrid",1,L,200,100,25,"solid",0.3393,k,"EXACT","Sec3.6")
# 15 Islam 2024 (RT-54HC/GNP+MWCNT) total 0.2wt%
add("Islam 2024","RT-54HC","none","base",0,0,0,"NR",25,"solid",0.20,0.20,"EXACT","Sec3.3")
add("Islam 2024","RT-54HC","GNP","carbon",0,0.2,4000,2000,25,"solid",0.20,0.23,"EXACT","Sec3.3")
add("Islam 2024","RT-54HC","GNP-MWCNT 1:1","hybrid",1,0.2,3500,"NR",25,"solid",0.20,0.25,"EXACT","Sec3.3")
add("Islam 2024","RT-54HC","GNP-MWCNT 1:3","hybrid",1,0.2,3500,"NR",25,"solid",0.20,0.28,"EXACT","Sec3.3")
add("Islam 2024","RT-54HC","GNP-MWCNT 3:1","hybrid",1,0.2,3500,"NR",25,"solid",0.20,0.26,"EXACT","Sec3.3")
add("Islam 2024","RT-54HC","MWCNT","carbon",0,0.2,3000,15,25,"solid",0.20,0.21,"EXACT","Sec3.3")
# 16 Ma 2022 (n-docosane+EG/Cu)
add("Ma 2022","n-docosane+EG","EG","carbon",0,15,100,"NR",25,"solid",1.182,1.182,"EXACT","Sec3.1")
add("Ma 2022","n-docosane+EG","Cu-EG","hybrid",1,16.7,250,"NR",25,"solid",1.182,1.983,"EXACT","Sec4")
# 17 Shama 2021 (paraffin/CuO)
for L,k in [(0,0.2864),(0.5,0.3227),(1,0.3360),(1.5,0.2198),(2,0.2398)]:
    add("Shama 2021","paraffin",("none" if L==0 else "CuO"),("base" if L==0 else "oxide"),0,L,(0 if L==0 else 33),52.7,20,"solid",0.2864,k,"EXACT","Table1")
# 18 Cui 2011 (soy wax + paraffin/CNF,MWCNT)
add("Cui 2011","soy wax","none","base",0,0,0,200,25,"solid",0.324,0.324,"EXACT","Table1")
for L,k in [(1,0.414),(2,0.426),(5,0.467),(10,0.469)]: add("Cui 2011","soy wax","CNF","carbon",0,L,2000,200,25,"solid",0.324,k,"EXACT","Table1")
for L,k in [(1,0.343),(2,0.354),(5,0.395),(10,0.403)]: add("Cui 2011","soy wax","MWCNT","carbon",0,L,3000,30,25,"solid",0.324,k,"EXACT","Table1")
add("Cui 2011","paraffin","none","base",0,0,0,200,25,"solid",0.320,0.320,"EXACT","Table2")
for L,k in [(1,0.398),(2,0.411),(5,0.439),(10,0.450)]: add("Cui 2011","paraffin","CNF","carbon",0,L,2000,200,25,"solid",0.320,k,"EXACT","Table2")
# 19 Energies 2026 (CrodaTherm/GNP)
add("Energies 2026","CrodaTherm 60","none","base",0,0,0,"NR",19,"solid",0.289,0.289,"EXACT","Table6")
for L,k in [(2,0.298),(4,0.307),(6,0.329)]: add("Energies 2026","CrodaTherm 60","GNP-1","carbon",0,L,4000,2,22,"solid",0.289,k,"EXACT","Table6")
for L,k in [(2,0.476),(4,0.687),(6,0.719)]: add("Energies 2026","CrodaTherm 60","GNP-2","carbon",0,L,4000,7,22,"solid",0.289,k,"EXACT","Table6")
# 20 Samara & Hamdan 2024 (paraffin/Al2O3) vol%->wt%(1vol=4wt,3vol=11wt), solid23/liq35/liq50
for T,ph,bk,vals in [(23,"solid",0.277,[(0,0.277),(4,0.307),(11,0.338)]),(35,"liquid",0.132,[(0,0.132),(4,0.146),(11,0.157)]),(50,"liquid",0.149,[(0,0.149),(4,0.167),(11,0.179)])]:
    for L,k in vals: add("Samara & Hamdan 2024","paraffin",("none" if L==0 else "Al2O3"),("base" if L==0 else "oxide"),0,L,(0 if L==0 else 35),80,T,ph,bk,k,"EXACT","Table1")

# 21 Zhang 2025 (paraffin/EG shape-stabilized, radial; base imputed 0.25)
add("Zhang 2025","paraffin","EG (SY skeleton)","carbon",0,10,100,"NR",25,"solid",0.25,10.70,"EXACT(base imp.)","text p.9 radial")
add("Zhang 2025","paraffin","EG (SH skeleton)","carbon",0,10,100,"NR",25,"solid",0.25,9.99,"EXACT(base imp.)","text p.9 radial")

for i,r in enumerate(rows,1): r["id"]=i
cols=["id","source","base_pcm","filler","filler_class","hybrid_flag","loading_wt","filler_k_WmK","particle_size_nm","temp_C","phase","base_k_WmK","keff_WmK","delta_k_pct","keff_source","where"]
with open("nepcm_databank.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader()
    for r in rows: w.writerow(r)
from collections import Counter
print("TOTAL rows:",len(rows))
print("unique sources:",len(set(r["source"] for r in rows)))
print("hybrid points:",sum(r["hybrid_flag"] for r in rows))
print("phases:",dict(Counter(r["phase"] for r in rows)))
print("keff range: %.3f – %.3f W/m/K"%(min(r["keff_WmK"] for r in rows),max(r["keff_WmK"] for r in rows)))
print("keff_source:",dict(Counter(r["keff_source"] for r in rows)))
