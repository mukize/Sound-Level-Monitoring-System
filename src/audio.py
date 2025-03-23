import numpy as np
import math


SAMPLE_RATE = 48000


def seconds_to_frames(seconds: float) -> int:
    return int(SAMPLE_RATE * seconds)


def signal_decibel(data: np.ndarray) -> float:
    rms = np.sqrt(np.mean(np.square(np.abs(data))))
    return 20 * math.log10(rms)
