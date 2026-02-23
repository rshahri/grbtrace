import numpy as np
from dataclasses import dataclass

@dataclass(frozen=True)
class T90Result:
    t90: float
    t5: float
    t95: float
    total_counts: float

def compute_t90(t: np.ndarray, counts: np.ndarray, start_idx: int, end_idx: int):
    """
    Compute T90 inside a detected window.
    T90 = time between 5% and 95% of cumulative counts in window.
    """
    t = np.asarray(t, dtype=float)
    counts = np.asarray(counts, dtype=float)

    window_t = t[start_idx:end_idx + 1]
    window_counts = counts[start_idx:end_idx + 1]

    cum = np.cumsum(window_counts)
    total = float(cum[-1])

    if total <= 0 or len(cum) < 2:
        return None

    t5 = float(np.interp(0.05 * total, cum, window_t))
    t95 = float(np.interp(0.95 * total, cum, window_t))
    t90 = float(t95 - t5)

    return T90Result(t90=t90, t5=t5, t95=t95, total_counts=total)

def peak_rate(counts: np.ndarray, dt: float) -> float:
    counts = np.asarray(counts, dtype=float)
    return float(np.max(counts) / dt)

def fluence_proxy(counts: np.ndarray) -> float:
    counts = np.asarray(counts, dtype=float)
    return float(np.sum(counts))