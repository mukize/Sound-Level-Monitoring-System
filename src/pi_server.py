from gpiozero import DigitalInputDevice
from dotenv import load_dotenv
from os import getenv
import socket
from util import CHANNEL, udp_socket

load_dotenv()
sensor = DigitalInputDevice(getenv("CHANNEL", CHANNEL))


def conn_handler(addr, sock: socket.socket):
    print(f"Sending data to {addr}")
    while True:
        if sensor.value:
            sock.sendto("Noise detected.".encode(), addr)
    print(f"Stopped sending data to {addr}")


try:
    sock = udp_socket(conn_handler)
except KeyboardInterrupt:
    pass
