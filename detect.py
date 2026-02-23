import numpy as np
from dataclasses import dataclass

@dataclass(frozen=True)
class DetectionResult:
    start_idx: int
    end_idx: int
    threshold: float
    bkg_median: float
    bkg_std_est: float

def detect_burst_threshold(counts: np.ndarray, sigma: float = 5.0):
    """
    Simple burst detection: detect contiguous region where counts exceed a robust threshold.

    Returns DetectionResult or None if no burst is detected.
    """
    counts = np.asarray(counts)

    med = float(np.median(counts))
    mad = float(np.median(np.abs(counts - med))) + 1e-12
    std = 1.4826 * mad  # MAD->std approx for normal dist
    threshold = med + sigma * std

    mask = counts > threshold
    if not np.any(mask):
        return None

    idx = np.where(mask)[0]
    start_idx, end_idx = int(idx[0]), int(idx[-1])

    return DetectionResult(
        start_idx=start_idx,
        end_idx=end_idx,
        threshold=float(threshold),
        bkg_median=med,
        bkg_std_est=float(std),
    )