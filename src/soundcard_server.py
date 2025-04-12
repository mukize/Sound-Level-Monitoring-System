import socket
from os import getenv

import soundcard as sc
from dotenv import load_dotenv
import util
from util import DEFAULT_SAMPLE_RATE, seconds_to_frames, signal_decibel

load_dotenv()
SAMPLE_RATE = getenv("SAMPLE_RATE", DEFAULT_SAMPLE_RATE)
INTERVAL = getenv("INTEVAL", 0.2)


def conn_handler(addr, sock: socket.socket):
    print(f"Sending data to {addr}")
    error = ""
    try:
        with sc.default_microphone().recorder(SAMPLE_RATE, channels=[0]) as mic:
            n_buffer_frames = seconds_to_frames(INTERVAL)
            while True:
                data = mic.record(n_buffer_frames).flatten()
                noise_detected = signal_decibel(data) > 50
                if noise_detected:
                    sock.sendto("Noise Detected.".encode(), addr)
    except Exception as e:
        error = e
    print(f"Stopped sending data to {addr} ({error})")


try:
    sock = util.udp_socket(conn_handler)
except KeyboardInterrupt:
    pass
