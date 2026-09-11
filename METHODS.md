# Methods (condensed — full detail in MANUSCRIPT.pdf §2)

1. **Radiometric IR survey** of the bare equipment — FLIR S62 Pro, ε = 0.90, reflected &
   atmospheric 25 °C, 50 % RH, ~3 m; per-pixel recompute from each file's raw thermal matrix
   (exiftool + raw2temp); ISO 18434-1 / ASTM E1933. single-flame-tube fire-tube steam boiler (≈6 t/h),
   13 Oct 2025, 38 measurements.
2. **CAD reconstruction** (SolidWorks) of bare and Inzonex-panelled models per equipment type;
   extract true outer surface area per component.
3. **+12 % surface allowance** for bolts, nuts, weld seams and irregularities — enters the
   heat-transfer area only (not insulation/fabrication quantity).
4. **ISO 12241 / ASTM C680** steady-state surface-temperature prediction (ideal 100 mm
   mineral-wool panel; λ = 0.045 W/m·K; h = 10 W/m²·K still air; ambient 25 °C):
   Ts = [ T_bare·(λ/t) + T_a·h ] / [ λ/t + h ].
5. **FLIR validation** of predicted vs measured insulated surface temperature; **ISO 13732-1**
   touch-safety classification (≤45 °C).
