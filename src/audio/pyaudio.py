import pyaudio
import numpy as np
from typing import Generator
from util import seconds_to_frames, signal_decibel, SAMPLE_RATE


def poll_noise_level(interval: float) -> Generator[float, None, None]:
    n_buffer_frames = seconds_to_frames(interval)
    with pyaudio.PyAudio().open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=n_buffer_frames,
    ) as stream:
        while True:
            data = np.frombuffer(stream.read(n_buffer_frames), dtype=np.float32)
            yield signal_decibel(data)


if __name__ == "__main__":
    try:
        for dB in poll_noise_level(0.2):
            print(round(dB, 2), "dB")
    except KeyboardInterrupt:
        pass
