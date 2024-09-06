import socket
import sys

# Function for the Server
def start_server(SERVER_IP, SERVER_PORT, BUFFER_SIZE, FILE_PATH):
    def send_file_to_client(connection):
        try:
            with open(FILE_PATH, "rb") as file:
                while True:
                    # Read file data in chunks
                    file_data = file.read(BUFFER_SIZE)
                    if not file_data:
                        break  # End of file
                    connection.sendall(file_data)
            print(f"File '{FILE_PATH}' sent successfully.")
        except Exception as e:
            print(f"Error sending file: {e}")
        finally:
            connection.close()

    # Create a TCP socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(1)
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        # Wait for a client connection
        connection, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        send_file_to_client(connection)

# Function for the Client
def start_client(CLIENT_IP, SERVER_PORT, BUFFER_SIZE, OUTPUT_FILE_PATH):
    def receive_file_from_server():
        try:
            # Create a TCP socket for the client
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((CLIENT_IP, SERVER_PORT))
            print(f"Connected to server {CLIENT_IP}:{SERVER_PORT}")

            with open(OUTPUT_FILE_PATH, "wb") as file:
                while True:
                    # Receive file data in chunks
                    file_data = client_socket.recv(BUFFER_SIZE)
                    if not file_data:
                        break  # No more data from server
                    file.write(file_data)
            print(f"File received and saved as '{OUTPUT_FILE_PATH}'.")
        except Exception as e:
            print(f"Error receiving file: {e}")
        finally:
            client_socket.close()

    receive_file_from_server()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py [server|client]")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "server":
        start_server("0.0.0.0", 5001, 1024, "TestProj/test.exe")
    elif mode == "client":
        start_client("127.0.0.1", 5001, 1024, "testing.exe")
    else:
        print("Invalid mode. Choose 'server' or 'client'.")
