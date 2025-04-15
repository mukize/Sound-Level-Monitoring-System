
#---Imports for socket programming and datetime usage---#
import socket 
import datetime

#---Initialisation of variables---#
SERVER_IP = "127.0.0.1"  
SERVER_PORT = 1234       
spikes = [] 


#---Main function to connect clients to server---#
def main(): 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                #Creates a client socket using UDP protocol for its faster communication speed
    server_address = (SERVER_IP, SERVER_PORT)                                       #Creates server address by combining server IP and port number
    print(f"Connecting to server: {SERVER_IP}, {SERVER_PORT} ...")
    client_socket.sendto("Joining Server".encode("utf-8"), server_address)          #Sends joining message to server
    try:
        while True:
            msg, _ = client_socket.recvfrom(1024)                                   #Receives message from server
            msg = msg.decode("utf-8")                                               #Decodes the message received from server
            if msg:                                                                 #Checks if the message is not empty, if not empty, it will be printed to screen
                currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #creates a timestamp for the noise detected using datetime module
                print(f"[{currentTime}] Noise Detected.")                 
                spikes.append(currentTime)                                          #Adds the timestamp to the spikes list
            else:                                                                   
                print(f"Server: {msg}")
    except KeyboardInterrupt:                                                       #except used to user to exit using Ctrl+C
        print("\nClient Requesting exit...")
    finally:                                                                        #finally block is used to close the socket connection and print the spikes detected during the session
        client_socket.close()
        print("Disconnected...")
        print("\nNoise Spikes Detected During Session:")
        for spike in spikes:
            print(spike)

if __name__ == "__main__":                                                          #Invokes the main function to start the program
    main()