# Effective Thermal Conductivity of Filler-Enhanced Phase Change Materials — Dataset and Code

This deposit contains the compiled dataset and the analysis code used to model the effective
thermal conductivity of filler- (nanoparticle-) enhanced phase change materials (PCMs) with
machine learning. It is released to support open reproducibility of the associated study.

The associated manuscript is not part of this deposit and is currently under peer review; only
openly shareable research artifacts (the compiled data and the analysis code) are included here.

## Contents

- `nepcm_databank.csv` — 150 effective-thermal-conductivity measurements compiled from 21 primary,
  previously published experimental studies. Every row is traceable to its source publication.
- `code/build_dataset.py` — assembles `nepcm_databank.csv` from the values extracted from the
  source publications.
- `code/run_pipeline.py` — feature engineering and the model training / cross-validation pipeline.
- `LICENSE` — Creative Commons Attribution 4.0 International (CC BY 4.0).
- `CITATION.cff` — machine-readable citation metadata (read automatically by Zenodo and GitHub).

## Dataset columns

| Column | Meaning |
|---|---|
| `id` | Row identifier |
| `source` | Citation of the primary experimental study the value is taken from |
| `base_pcm` | Base phase change material |
| `filler` | Filler / additive (`none` for a pure base measurement) |
| `filler_class` | Filler family (carbon, oxide, metal, carbide, hybrid, base) |
| `hybrid_flag` | 1 if a two-filler (hybrid) system, else 0 |
| `loading_wt` | Filler loading (wt %) |
| `filler_k_WmK` | Intrinsic thermal conductivity of the filler (W m^-1 K^-1) |
| `particle_size_nm` | Reported particle size (nm; `NR` = not reported) |
| `temp_C` | Measurement temperature (deg C) |
| `phase` | Physical state at measurement (`solid` / `liquid`) |
| `base_k_WmK` | Thermal conductivity of the base material (W m^-1 K^-1) |
| `keff_WmK` | Measured effective thermal conductivity (W m^-1 K^-1) |
| `delta_k_pct` | Percentage change in conductivity relative to the base |
| `keff_source` | `EXACT` = value quoted in the source; `COMPUTED` = derived from a reported % enhancement; base-imputed rows are flagged |
| `where` | Location of the value in the source document (table / figure / page) |

All measurements originate from the cited, publicly available primary literature. This deposit
redistributes them in aggregated, attributed tabular form for reproducibility. Users should cite
both this deposit and the original studies listed in the `source` column.

## What the code does

`run_pipeline.py` engineers five physically motivated inputs — filler loading, a filler/base
conductivity-contrast term log10(1 + k_f / k0), temperature, phase, and a hybrid-system flag — and
models the logarithmic enhancement target y = log10(k_eff / k_base). Five regressors (linear
regression, support-vector regression, random forest, gradient boosting and a small neural network)
are trained and compared under leakage-free 10-fold cross-validation, with a leave-one-source-out
check for cross-study transfer. Running the script prints the cross-validated metrics.

## Reproduce

```bash
pip install numpy pandas scikit-learn
python code/build_dataset.py    # writes nepcm_databank.csv
python code/run_pipeline.py     # trains and validates the models; prints metrics
```

Requirements: Python 3.9+, numpy, pandas, scikit-learn.

## License

This dataset and code are released under the Creative Commons Attribution 4.0 International
(CC BY 4.0) license; see `LICENSE`. You are free to share and adapt the material for any purpose,
provided you give appropriate credit. Copyright (c) 2026 Muhammed Anaz Khan.

## Citation

If you use this 