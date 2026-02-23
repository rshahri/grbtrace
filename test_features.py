import os, sys

# Make src importable in Colab
sys.path.insert(0, os.path.abspath("grbtrace/src"))

from grbtrace.simulate import simulate_binned_lightcurve
from grbtrace.detect import detect_burst_threshold
from grbtrace.features import compute_t90

def test_t90_reasonable_for_simulation():
    t, counts, dt = simulate_binned_lightcurve(seed=7)
    det = detect_burst_threshold(counts, sigma=5.0)

    assert det is not None, "Burst should be detected in the default simulation."

    t90res = compute_t90(t, counts, det.start_idx, det.end_idx)
    assert t90res is not None, "T90 should be computable."

    # Sanity range for THIS simulation setup (not physics-truth, just regression safety)
    assert 0.5 < t90res.t90 < 6.0, f"T90 looks unreasonable: {t90res.t90}"