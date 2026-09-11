# -*- coding: utf-8 -*-
"""
Figures for the surface-temperature data-descriptor (no economics — surface temps only).
Fig1 method workflow; Fig2 bare vs insulated surface temp + 45C touch-safe line;
Fig3 model (ISO 12241 ideal 100 mm panel) vs FLIR-measured insulated surface temp.
"""
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.edgecolor":"#333",
                     "axes.linewidth":0.8,"figure.dpi":300})

ELEM = ["Front door", "Burner flange", "Steam valves"]
T_BARE = [96, 146, 190]
T_MEAS = [30, 30, 36]          # FLIR-measured insulated outer surface (deg C)
TOUCH = 45                      # ISO 13732-1 prolonged-contact safe limit

# model: ISO 12241 / C680 ideal continuous 100 mm mineral-wool panel
LAM, THK, HO, TA = 0.045, 0.10, 10.0, 25.0   # ambient 25 C (unified with the ROI model / live viz)
def model_surface(thot):
    k = LAM/THK
    return (thot*k + HO*TA)/(k+HO)
T_MODEL = [round(model_surface(t),1) for t in T_BARE]

C_BARE, C_INS, C_MODEL = "#c0392b", "#0e8a47", "#b08400"

# ---------- Fig 1: method workflow ----------
fig, ax = plt.subplots(figsize=(9.2,2.5))
ax.axis("off"); ax.set_xlim(0,10); ax.set_ylim(0,2)
steps = ["Radiometric\nIR survey\n(bare)",
         "CAD reconstruction\nbare + panelled\nmodels",
         "Surface-area\nextraction\n(+12% irregular.)",
         "ISO 12241 detailed\nsurface-temp\nprediction",
         "FLIR validation +\nISO 13732-1\ntouch-safety"]
w, gap = 1.7, 0.28; x = 0.15
for i,s in enumerate(steps):
    box = FancyBboxPatch((x,0.45), w, 1.1, boxstyle="round,pad=0.04,rounding_size=0.10",
                         linewidth=1.1, edgecolor="#333", facecolor="#f4f1e9")
    ax.add_patch(box)
    ax.text(x+w/2, 1.0, s, ha="center", va="center", fontsize=9)
    if i < len(steps)-1:
        ax.add_patch(FancyArrowPatch((x+w,1.0),(x+w+gap,1.0),arrowstyle="-|>",
                     mutation_scale=13, lw=1.3, color="#b08400"))
    x += w+gap
ax.text(5.0, 1.85, "Equipment-agnostic per-component method", ha="center", fontsize=10, style="italic", color="#555")
fig.tight_layout(); fig.savefig(os.path.join(OUT,"fig1_method.png"), bbox_inches="tight"); plt.close(fig)

# ---------- Fig 2: bare vs insulated surface temperature ----------
fig, ax = plt.subplots(figsize=(7.2,4.3))
x = np.arange(len(ELEM)); bw = 0.36
ax.bar(x-bw/2, T_BARE, bw, label="Bare (FLIR)", color=C_BARE)
ax.bar(x+bw/2, T_MEAS, bw, label="Insulated (FLIR)", color=C_INS)
ax.axhline(TOUCH, ls="--", lw=1.3, color="#1f6feb")
ax.text(len(ELEM)-0.5, TOUCH+5, "45 °C touch-safe (ISO 13732-1)", color="#1f6feb", fontsize=9, ha="right")
for i,(b,m) in enumerate(zip(T_BARE,T_MEAS)):
    ax.text(i-bw/2, b+3, f"{b}", ha="center", fontsize=9, color=C_BARE, fontweight="bold")
    ax.text(i+bw/2, m+3, f"{m}", ha="center", fontsize=9, color=C_INS, fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(ELEM); ax.set_ylabel("Outer-surface temperature (°C)")
ax.set_ylim(0,210); ax.legend(frameon=False, loc="upper left")
ax.set_title("Surface temperature before vs after removable modular insulation", fontsize=11)
ax.spines[["top","right"]].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT,"fig2_surface_temps.png"), bbox_inches="tight"); plt.close(fig)

# ---------- Fig 3: model vs measured insulated surface temp ----------
fig, ax = plt.subplots(figsize=(5.6,5.2))
ax.plot([0,50],[0,50], ls="--", color="#888", lw=1, label="1:1 (perfect agreement)")
ax.axhline(TOUCH, ls=":", color="#1f6feb", lw=1); ax.axvline(TOUCH, ls=":", color="#1f6feb", lw=1)
ax.scatter(T_MODEL, T_MEAS, s=90, color=C_MODEL, edgecolor="#333", zorder=5)
for i,e in enumerate(ELEM):
    ax.annotate(e, (T_MODEL[i], T_MEAS[i]), textcoords="offset points", xytext=(8,-3), fontsize=9)
ax.set_xlabel("Model — ISO 12241 ideal 100 mm panel (°C)")
ax.set_ylabel("FLIR-measured insulated surface (°C)")
ax.set_xlim(15,50); ax.set_ylim(15,50)
ax.set_title("Model vs measured insulated surface temperature", fontsize=11)
ax.text(46,46.5,"touch-safe\nzone", color="#1f6feb", fontsize=8, ha="right")
ax.legend(frameon=False, loc="lower right", fontsize=9)
ax.spines[["top","right"]].set_visible(False)
fig.tight_layout(); fig.savefig(os.path.join(OUT,"fig3_model_vs_measured.png"), bbox_inches="tight"); plt.close(fig)

print("model insulated surface temps (deg C):", T_MODEL)
print("measured insulated:", T_MEAS, "| all <= 45:", all(t<=45 for t in T_MEAS))
print("figures written to", OUT)
