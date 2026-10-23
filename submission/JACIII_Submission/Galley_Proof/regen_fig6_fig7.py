"""
Regenerate Fig. 6 and Fig. 7 of JACIII Jc26-0016 at the galley-proof stage.
Copied from experiment/generate_pdf_figures.py; ONLY the data values (and, for
Fig. 7, the bar labels that described the wrong configurations) are changed.
  Fig. 6: TC+TD bars use Table 2 "Best TC+TD" instead of Best TC + Best TD.
  Fig. 7: bars use Table 4 exactly; placeholder values removed.
"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = sys.argv[1] if len(sys.argv) > 1 else "."


def save_model_comparison_bar(out_path):
    models = [
        "Dual PubMedBERT\n(α=0.45, β=0.40)",
        "Hybrid\nPubMedBERT-BioBERT\n(α=0.30, β=0.35)",
        "Dual MiniLM\n(baseline)",
        "Dual BioBERT\n(α=0.45, β=0.80)",
    ]
    tc_vals  = [0.6172, 0.6038, 0.6076, 0.5826]
    td_vals  = [0.7458, 0.7333, 0.7143, 0.7000]
    sum_vals = [1.3443, 1.3247, 1.3005, 1.2331]   # CHANGED: Table 2 Best TC+TD

    baseline_sum = 1.2530   # reference model 3

    x    = np.arange(len(models))
    w    = 0.25

    fig, ax = plt.subplots(figsize=(13, 7))
    bars_tc  = ax.bar(x - w,     tc_vals,  width=w, label="TC",      color="#4C72B0", edgecolor="white")
    bars_td  = ax.bar(x,         td_vals,  width=w, label="TD",      color="#DD8452", edgecolor="white")
    bars_sum = ax.bar(x + w,     sum_vals, width=w, label="TC+TD",   color="#55A868", edgecolor="white")

    ax.axhline(y=baseline_sum, color="red", linestyle="--", linewidth=1.8,
               label=f"Baseline TC+TD ({baseline_sum:.4f})")

    for bar in bars_sum:
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.005,
                f"{bar.get_height():.4f}",
                ha="center", va="bottom", fontsize=10, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=12)
    ax.set_ylabel("Score", fontsize=14)
    ax.set_title("Best TC, TD, and TC+TD per Model Configuration\n"
                 "(Full text: Title + Abstract + MeSH)",
                 fontsize=15, pad=10)
    ax.set_ylim(0, max(sum_vals) * 1.12)
    ax.tick_params(axis="y", labelsize=12)
    ax.legend(fontsize=12, loc="upper right")
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_path, format="pdf", bbox_inches="tight")
    plt.savefig(out_path.replace(".pdf", "_preview.png"), dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {out_path}")


def save_ablation_bar(out_path):
    configs = [                                    # CHANGED: Table 4 configurations
        "Baseline\n(all-MiniLM\nsingle-stream)",
        "A1: Abstract only",
        "A2: Title +\nAbstract",
        "A3: Abstract +\nMeSH",
        "A4: Title +\nAbstract + MeSH",
        "Dual-stream\n(Full + α–β fusion)",
    ]
    tc_vals  = [0.5360, 0.5428, 0.5355, 0.5274, 0.5451, 0.6047]   # CHANGED: Table 4
    td_vals  = [0.7170, 0.7136, 0.6667, 0.6087, 0.6174, 0.6958]   # CHANGED: Table 4
    sum_vals = [1.2530, 1.2564, 1.2022, 1.1361, 1.1625, 1.3005]   # CHANGED: Table 4

    x = np.arange(len(configs))
    w = 0.25

    fig, ax = plt.subplots(figsize=(14, 7))
    ax.bar(x - w, tc_vals,  width=w, label="TC",    color="#4C72B0", edgecolor="white")
    ax.bar(x,     td_vals,  width=w, label="TD",    color="#DD8452", edgecolor="white")
    bars_s = ax.bar(x + w, sum_vals, width=w, label="TC+TD", color="#55A868", edgecolor="white")

    for bar in bars_s:
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.005,
                f"{bar.get_height():.4f}",
                ha="center", va="bottom", fontsize=9, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(configs, fontsize=11)
    ax.set_ylabel("Score", fontsize=14)
    ax.set_title("Ablation Study: TC, TD, and TC+TD\nfor Different Configurations",
                 fontsize=15, pad=10)
    ax.set_ylim(0, max(sum_vals) * 1.12)
    ax.tick_params(axis="y", labelsize=12)
    ax.legend(fontsize=12, loc="upper left")
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_path, format="pdf", bbox_inches="tight")
    plt.savefig(out_path.replace(".pdf", "_preview.png"), dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {out_path}")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    save_model_comparison_bar(os.path.join(OUT, "fig_model_comparison_bar.pdf"))
    save_ablation_bar(os.path.join(OUT, "fig_ablation_comparison.pdf"))
