import numpy as np

def simulate_binned_lightcurve(
    duration: float = 40.0,
    dt: float = 0.064,
    background_rate: float = 200.0,   # counts/sec
    burst_peak_rate: float = 2000.0,  # counts/sec
    burst_t0: float = 20.0,
    burst_sigma: float = 0.8,
    seed: int = 7,
):
    """
    Returns (t, counts, dt) where:
    - t: time array (seconds), one per bin
    - counts: Poisson counts per bin
    - dt: bin width (seconds)
    """
    rng = np.random.default_rng(seed)
    t = np.arange(0, duration, dt)

    bkg = np.full_like(t, background_rate)
    burst = burst_peak_rate * np.exp(-0.5 * ((t - burst_t0) / burst_sigma) ** 2)

    rate = bkg + burst
    expected_counts = rate * dt
    counts = rng.poisson(expected_counts)

    return t, counts, dt