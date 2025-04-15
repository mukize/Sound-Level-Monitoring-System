import socket
import datetime

SERVER_IP = "127.0.0.1"  
SERVER_PORT = 1234       
spikes = [] 

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (SERVER_IP, SERVER_PORT)
    print(f"Connecting to server: {SERVER_IP}, {SERVER_PORT} ...")
    client_socket.sendto("Joining Server".encode("utf-8"), server_address)
    try:
        while True:
            msg, _ = client_socket.recvfrom(1024)
            msg = msg.decode("utf-8")
            if msg == "Noise Detected.":
                currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{currentTime}] Noise Detected.")
                spikes.append(currentTime)
            else:
                print(f"Server: {msg}")
    except KeyboardInterrupt:
        print("\nClient Requesting exit...")
    finally:
        client_socket.close()
        print("Disconnected...")
        print("\nNoise Spikes Detected During Session:")
        for spike in spikes:
            print(spike)

if __name__ == "__main__":
    main()