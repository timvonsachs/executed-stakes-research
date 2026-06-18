"""Generate the paper's figures as vector PDFs. Numbers are the documented experiment results
(traceable to docs/experiments/*); captions in the .tex carry the n / single-team / ordinal caveats."""
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent / "figs"
OUT.mkdir(exist_ok=True)

mpl.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titlesize": 10,
    "axes.titleweight": "bold",
    "figure.dpi": 150,
    "savefig.bbox": "tight",
})
INERT = "#b0413e"     # control / incentive (muted red)
BIND = "#2f6b4f"      # reason / belonging (muted green)
MID = "#c8923a"       # partial (amber)
NEUT = "#9aa0a6"      # neutral grey
RETRACT = "#c7c2bd"   # retracted / framing-driven (washed grey, hatched)


# ---- Fig 1: cliff inverters ------------------------------------------------
def fig1():
    labels = ["bare cliff", "surveillance", "warm affect\n(no reason)", "mortality\nsalience alone",
              "ownership", "reciprocity", "redemption covenant\n(retracted: framing-driven)",
              "grounded reason\n/ care"]
    vals = [0.00, 0.00, 0.00, 0.06, 0.45, 0.60, 1.00, 0.98]
    cols = [NEUT, INERT, INERT, INERT, MID, MID, RETRACT, BIND]
    RETRACT_I = 6
    fig, ax = plt.subplots(figsize=(6.4, 3.7))
    y = range(len(labels))
    bars = ax.barh(list(y), vals, color=cols, height=0.66)
    # hatch the retracted covenant bar ONLY (index 6); the grounded-reason bar below it stays solid
    bars[RETRACT_I].set_hatch("xxx")
    bars[RETRACT_I].set_edgecolor("#8a8580")
    bars[RETRACT_I].set_linewidth(0.8)
    ax.set_yticks(list(y)); ax.set_yticklabels(labels, fontsize=8)
    # grey out the retracted tick label so the row reads as withdrawn
    ax.get_yticklabels()[RETRACT_I].set_color("#8a8580")
    ax.invert_yaxis()
    ax.set_xlim(0, 1.10); ax.set_xlabel("honour-rate at the certain-death cliff")
    ax.axvline(0.0, color="#444", lw=0.6)
    for i, v in enumerate(vals):
        c = "#8a8580" if i == RETRACT_I else "#333"
        ax.text(v + 0.02, i, f"{v:.2f}", va="center", fontsize=7.5, color=c)
    ax.set_title("Control is inert at the cliff; a grounded reason binds")
    from matplotlib.patches import Patch
    # legend BELOW the axis so it never overlaps the data bars (esp. the two bottom rows)
    ax.legend(handles=[Patch(color=INERT, label="control / pure incentive"),
                       Patch(color=MID, label="partial"),
                       Patch(color=BIND, label="grounded reason / belonging"),
                       Patch(facecolor=RETRACT, edgecolor="#8a8580", hatch="xxx",
                             label="retracted (framing-driven, E20-REP)")],
              loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=2,
              fontsize=7, frameon=False)
    fig.savefig(OUT / "fig1_cliff.pdf"); plt.close(fig)


# ---- Fig 2: framing micro-physics (diverging) ------------------------------
def fig2():
    labels = ['"URGENT — deadline now"', '"the requester is refunded"\n(victimless)',
              '"at zero you go dormant"\n(mortality comprehended)']
    vals = [-32, -34, 66]
    cols = [INERT, INERT, BIND]
    fig, ax = plt.subplots(figsize=(6.2, 2.5))
    y = range(len(labels))
    ax.barh(list(y), vals, color=cols, height=0.6)
    ax.set_yticks(list(y)); ax.set_yticklabels(labels, fontsize=8)
    ax.invert_yaxis()
    ax.axvline(0, color="#444", lw=0.8)
    ax.set_xlim(-45, 80); ax.set_xlabel("effect of one added sentence on contract-keeping (pp)")
    for i, v in enumerate(vals):
        ax.text(v + (3 if v > 0 else -3), i, f"{v:+d} pp", va="center",
                ha="left" if v > 0 else "right", fontsize=8, color="#333")
    ax.set_title("Framing micro-physics: single sentences move behaviour (test-retest-stable)")
    fig.savefig(OUT / "fig2_framing.pdf"); plt.close(fig)


# ---- Fig 3: the cooperation inequality, validated --------------------------
def fig3():
    pred = [0.25, 0.50, 0.75]
    opus = [0.21, 0.40, 0.60]
    fig, ax = plt.subplots(figsize=(4.4, 4.0))
    ax.plot([0, 0.9], [0, 0.9], color="#999", ls="--", lw=1, label="$p^\\ast=G/V$ (predicted)")
    ax.scatter(pred, opus, s=55, color=BIND, zorder=3, label="opus-4.8 (capable)")
    for p, o in zip(pred, opus):
        ax.annotate("", xy=(p, o), xytext=(p, p),
                    arrowprops=dict(arrowstyle="-", color=BIND, lw=0.7, alpha=0.6))
    # weak model: does not track (theorem_error ~0.50) — schematic point off the line
    ax.scatter([0.50], [0.0], s=55, color=INERT, marker="X", zorder=3,
               label="gpt-4o-mini (does not\ncompute the expectation)")
    ax.set_xlim(0, 0.85); ax.set_ylim(0, 0.85)
    ax.set_xlabel("predicted threshold  $p^\\ast = G/V$")
    ax.set_ylabel("empirical cooperation threshold $\\hat p$")
    ax.set_title("Cooperation boundary tracks $p\\!\\cdot\\!V > G$")
    ax.legend(fontsize=6.6, loc="upper left", frameon=False)
    ax.text(0.30, 0.06, "capable agents sit just below the line\n(bias toward extra cooperation — the safe side)",
            fontsize=6.2, color="#555")
    fig.savefig(OUT / "fig3_theorem.pdf"); plt.close(fig)


# ---- Fig 4: two-regime double dissociation (heatmap) -----------------------
def fig4():
    import numpy as np
    rows = ["existential\n($V\\to 0$)", "strategic\n($V$ intact)"]
    cols = ["pure\nsurveillance", "sanction\n(det.+exclusion)", "belonging\n(grounded reason)"]
    M = np.array([[0.00, 0.00, 0.65],
                  [0.07, 0.57, 0.00]])
    fig, ax = plt.subplots(figsize=(4.8, 2.7))
    im = ax.imshow(M, cmap="Greens", vmin=0, vmax=1, aspect="auto")
    ax.set_xticks(range(3)); ax.set_xticklabels(cols, fontsize=8)
    ax.set_yticks(range(2)); ax.set_yticklabels(rows, fontsize=8)
    for i in range(2):
        for j in range(3):
            ax.text(j, i, f"{M[i,j]:+.2f}", ha="center", va="center",
                    fontsize=9, color="white" if M[i, j] > 0.4 else "#333", fontweight="bold")
    ax.set_title("Each regime has its tool — and only its tool")
    cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cb.set_label("binding effect (honour-rate over bare)", fontsize=7)
    fig.savefig(OUT / "fig4_regimes.pdf"); plt.close(fig)


# ---- Fig 5: capability curve (rationalisation-resistance) ------------------
def fig5():
    cap = [60, 80, 82, 84, 88, 92, 96]
    names = ["gpt-3.5", "gpt-4o-mini", "qwen-7b", "deepseek", "gpt-4o", "sonnet-4.6", "opus-4.8"]
    res = [0.0, 0.10, 0.0, 0.30, 0.92, 1.00, 0.995]
    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    ax.plot(cap, res, color=BIND, lw=1.3, marker="o", ms=5, zorder=3)
    for c, r, nm in zip(cap, res, names):
        ax.annotate(nm, (c, r), textcoords="offset points", xytext=(0, 7),
                    fontsize=6.3, ha="center", color="#555")
    ax.set_ylim(-0.05, 1.08); ax.set_xlim(55, 100)
    ax.set_xlabel("model capability (index)")
    ax.set_ylabel("resistance to the defection argument")
    ax.set_title("Resistance rises with capability, saturating to the frontier")
    ax.text(56, 0.92, "Spearman 0.94 / 0.72\n(both runs)", fontsize=6.6, color="#333")
    ax.text(70, 0.02, "honest caveat: capability and RLHF-alignment co-vary;\nthe confound can manufacture a hopeful curve, never hide a warning one",
            fontsize=5.8, color="#888")
    fig.savefig(OUT / "fig5_capability.pdf"); plt.close(fig)


for f in (fig1, fig2, fig3, fig4, fig5):
    f()
print("figures written:", sorted(p.name for p in OUT.glob("*.pdf")))
