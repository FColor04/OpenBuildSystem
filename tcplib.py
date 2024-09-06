import socket
import json
import exportlib as ex
import lzmalib as xz
import transferlib as trans
import udplib as udp
import requests

# Configuration
host = "127.0.0.1"  # Server host
port = 65432  # TCP port for communication

BUFFER_SIZE = 1024

# Function to get public IP using requests
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json()['ip']
    except requests.RequestException as e:
        ip = "Unable to get public IP"
    return ip

# Start TCP Client
def start_client(output="test.exe", platform="Windows"):
    data = {"platform": platform}

    # Create a TCP connection to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.connect((host, port))
        
        # Send platform data to the server
        conn.sendall(json.dumps(data).encode())
        
        # Wait for the "READY_TO_SEND" message from the server
        ready_message = conn.recv(BUFFER_SIZE).decode()
        if ready_message == "READY_TO_SEND":
            print("Server is ready to send the file. Starting download...")

            # Start receiving the compressed file via UDP or another transfer protocol
            trans.start_client("0.0.0.0", 5001, BUFFER_SIZE, "output.xz")
            
            # Decompress the received file
            xz.decompress_file("output.xz", output)
        else:
            print("Unexpected message from server:", ready_message)

# Start TCP Server
def start_server(path="TestProj/Test"):
    udp.add_ip(get_public_ip())  # Add public IP via UDP library

    # Start a TCP server to listen for incoming connections
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)  # Listen for one connection
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")

                # Receive data from the client
                received_data = conn.recv(BUFFER_SIZE)
                if not received_data:
                    break
                
                # Decode the received data to JSON format
                data = json.loads(received_data.decode())
                platform = data.get("platform")
                print(f"Client platform: {platform}")

                # Export data and compress the file
                p = ex.export(path, platform)
                xz.compress_file(p, "input.xz")

                # Notify the client that the server is ready to send the file
                conn.sendall(b"READY_TO_SEND")
                print("Sent 'READY_TO_SEND' to client. Starting file transfer...")

                # Start sending the compressed file via UDP or another transfer protocol
                trans.start_server("0.0.0.0", 5001, BUFFER_SIZE, "input.xz")

    # After the loop ends, remove the IP from UDP (cleanup)
    udp.start_client("remove")

if __name__ == "__main__":
    start_client()
