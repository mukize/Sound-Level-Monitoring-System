import socket
import numpy as np
import math
import soundcard as sc
import util


def signal_decibel(data: np.ndarray) -> float:
    """
    Calculate the decibel sound pressure level from raw signal data.
    """
    rms = np.sqrt(np.mean(np.square(np.abs(data))))
    return 20 * math.log10(rms / 20e-6)


def main():
    sample_rate = 48000
    mic = sc.default_microphone().recorder(sample_rate, channels=[0])

    def conn_handler(addr, sock: socket.socket):
        print(f"Sending data to {addr}")
        error = ""
        try:
            n_buffer_frames = int(sample_rate * 0.2)
            while True:
                data = mic.record(n_buffer_frames).flatten()
                noise_detected = signal_decibel(data) > 50
                if noise_detected:
                    sock.sendto("Noise Detected.".encode(), addr)
        except Exception as e:
            error = e
        print(f"Stopped sending data to {addr} ({error})")

    try:
        util.udp_socket(conn_handler)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
