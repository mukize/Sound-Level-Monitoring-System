import numpy as np
import math


DEFAULT_SAMPLE_RATE: int = 48000


def seconds_to_frames(seconds: float, sample_rate=DEFAULT_SAMPLE_RATE) -> int:
    return int(DEFAULT_SAMPLE_RATE * seconds)


def signal_decibel(data: np.ndarray) -> float:
    rms = np.sqrt(np.mean(np.square(np.abs(data))))
    return 20 * math.log10(rms)
