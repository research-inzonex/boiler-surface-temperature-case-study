# Surface-temperature dataset: modular removable insulation

Field-validated component-level dataset for predicting the outer-surface temperature of modular
removable insulation on irregular industrial equipment. The study covers one approximately 6 t/h
single-flame-tube fire-tube steam boiler surveyed in 2025. It is a single-equipment case study,
not a universal product-performance dataset.

## Persistent records

- Dataset, current version (v2.0): https://doi.org/10.5281/zenodo.21810802
- Preprint on Zenodo: https://doi.org/10.5281/zenodo.20832589
- Preprint on engrXiv: https://doi.org/10.31224/7444
- Calculation methodology: https://inzonex.co.uk/calc/methodology/

The Zenodo record is the citable version of record. Cite the DOI, not this repository.

## Authors

| Author | ORCID |
|---|---|
| Dmytro Aheiev | 0009-0001-5512-0291 |
| Artem Gunin | 0009-0007-7853-3244 |
| Danylo Kruhlov | 0009-0003-2313-7923 |
| Nataliia Bilous | 0009-0003-0877-4940 |
| Pavlo Didenko | 0009-0008-8546-0052 |

Affiliation: Inzonex. License: CC BY 4.0.

## Public dataset

`data/surface_temperatures.csv` contains three component-level summary records: front door, boiler
burner flange and steam valves. The columns separate CAD area, the documented 12% geometric
allowance, FLIR-measured bare and insulated temperatures, ISO 12241 model output, ambient
temperature, ISO 13732-1 touch-safety classification and excess-temperature reduction.

Run the deterministic check before packaging:

```
python build_dataset.py --check
```

This reproduces the deposited 391-byte CSV exactly. It contains no energy-price, operating-hours,
CO2 or payback assumptions.

## Files

| File | What |
|---|---|
| `data/surface_temperatures.csv` | Public component summary dataset |
| `build_dataset.py` | Deterministic CSV builder and byte-level check |
| `build_figures.py` | Reproducible figure builder |
| `figures/fig1_method.png` | Study workflow |
| `figures/fig2_surface_temps.png` | Measured bare/insulated temperatures |
| `figures/fig3_model_vs_measured.png` | Model/measurement comparison |
| `METHODS.md` | Condensed method |
| `LICENSE` | CC BY 4.0 |

The manuscript itself is not mirrored here; read it at the preprint DOIs above.

## Scope and availability

The public CSV contains three component summaries derived from 38 pixel-level measurements. Raw
radiometric TIFF files are retained by Inzonex under controlled access because they include project
records. Verification requests may be sent to contact@inzonex.co.uk.
