import numpy as np
import matplotlib.pyplot as plt

def plot_lightcurve(t, counts, threshold=None, window=None, title="Light curve"):
    t = np.asarray(t)
    counts = np.asarray(counts)

    plt.figure(figsize=(12, 4))
    plt.step(t, counts, where="mid", linewidth=1.0)
    plt.xlabel("time (s)")
    plt.ylabel("counts / bin")
    plt.title(title)

    if threshold is not None:
        plt.axhline(threshold, linestyle="--", linewidth=1.0, label=f"threshold={threshold:.1f}")

    if window is not None:
        t0, t1 = window
        plt.axvspan(t0, t1, alpha=0.2, label="detected window")

    if threshold is not None or window is not None:
        plt.legend()

    plt.tight_layout()
    plt.show()