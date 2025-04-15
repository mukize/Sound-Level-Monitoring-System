from dotenv import load_dotenv
import os
import socket
import concurrent.futures
from typing import Callable


DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = "1234"


def udp_socket(connection_handler: Callable[[tuple, socket.socket], None]):
    """
    Create a udp socket and run handler for each connection.
    """
    load_dotenv()
    host = os.getenv("SERVER_HOST", DEFAULT_HOST)
    port = int(os.getenv("SERVER_PORT", DEFAULT_PORT))

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((host, port))
        print(f"Listening on {host}:{port}")
        # get a pool of thread workers
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
            while True:
                _, addr = sock.recvfrom(1024)
                pool.submit(connection_handler, addr, sock)
