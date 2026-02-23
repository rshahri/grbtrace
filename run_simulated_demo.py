import sys
import os

# Make src importable in Colab
sys.path.insert(0, os.path.abspath("grbtrace/src"))

from grbtrace.simulate import simulate_binned_lightcurve
from grbtrace.detect import detect_burst_threshold
from grbtrace.features import compute_t90, peak_rate, fluence_proxy
from grbtrace.plot import plot_lightcurve

def main():
    t, counts, dt = simulate_binned_lightcurve()

    det = detect_burst_threshold(counts, sigma=5.0)

    if det is None:
        print("No burst detected.")
        plot_lightcurve(t, counts, title="Simulated light curve (no detection)")
        return

    window = (t[det.start_idx], t[det.end_idx])
    t90res = compute_t90(t, counts, det.start_idx, det.end_idx)

    plot_lightcurve(
        t, counts,
        threshold=det.threshold,
        window=window,
        title="Simulated GRB light curve + detection"
    )

    print("=== Detection ===")
    print(f"Window: {window[0]:.3f}s → {window[1]:.3f}s")
    print(f"Threshold: {det.threshold:.2f} (median={det.bkg_median:.2f}, std_est={det.bkg_std_est:.2f})")

    print("\n=== Features ===")
    if t90res is None:
        print("T90 could not be computed.")
    else:
        print(f"T90: {t90res.t90:.3f}s (t5={t90res.t5:.3f}s, t95={t90res.t95:.3f}s)")
        print(f"Total counts in window: {t90res.total_counts:.0f}")

    print(f"Peak rate (global): {peak_rate(counts, dt):.1f} counts/s")
    print(f"Fluence proxy (global): {fluence_proxy(counts):.0f} counts")

if __name__ == "__main__":
    main()