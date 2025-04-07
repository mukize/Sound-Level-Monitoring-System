import socket
import concurrent.futures
from audio.soundcard import poll_noise_level

HOST = "127.0.0.1"
PORT = 1234


def connection_handler(addr, sock: socket.socket):
    print(f"Sending data to {addr}")
    break_message = ""
    for dB in poll_noise_level(0.2):
        try:
            sock.sendto(str(dB).encode(), addr)
        except Exception as e:
            break_message = e
            break
    print(f"Stopped sending data to {addr} ({break_message})")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, PORT))
        print(f"Listening on {HOST}:{PORT}")
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
            while True:
                _, addr = sock.recvfrom(1024)
                pool.submit(connection_handler, addr, sock)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
