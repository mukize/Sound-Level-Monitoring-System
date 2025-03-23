import soundcard as sc
from typing import Generator
from audio import seconds_to_frames, signal_decibel, SAMPLE_RATE


def poll_noise_level(interval: float) -> Generator[float, None, None]:
    with sc.default_microphone().recorder(SAMPLE_RATE, channels=[0]) as mic:
        n_buffer_frames = seconds_to_frames(interval)
        while True:
            data = mic.record(n_buffer_frames).flatten()
            yield signal_decibel(data)


if __name__ == "__main__":
    try:
        for dB in poll_noise_level(0.2):
            print(round(dB, 2), "dB")
    except KeyboardInterrupt:
        pass
