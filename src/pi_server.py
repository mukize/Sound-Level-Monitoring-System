from gpiozero import DigitalInputDevice
from dotenv import load_dotenv
from os import getenv
import socket
from util import DEFAULT_CHANNEL, udp_socket


def main():
    load_dotenv()
    sensor = DigitalInputDevice(getenv("CHANNEL", DEFAULT_CHANNEL))

    def conn_handler(addr, sock: socket.socket):
        print(f"Sending data to {addr}")
        while True:
            if sensor.value:
                sock.sendto("Noise detected.".encode(), addr)
        print(f"Stopped sending data to {addr}")

    try:
        udp_socket(conn_handler)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
