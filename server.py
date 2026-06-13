import socket

HOST = "127.0.0.1"
PORT = 5050

def start_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        print(f"Server listening on {HOST}:{PORT}")
        print("Waiting for a client to connect...")

        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        while True:
            data = conn.recv(1024)

            if not data:
                print("Client disconnected.")
                break

            message = data.decode()
            print(f"Client says: {message}")

            if message.lower() == "bye":
                conn.sendall("Goodbye! Closing connection.".encode())
                break

            response = f"Server received your message: {message}"
            conn.sendall(response.encode())

        conn.close()
        server_socket.close()
        print("Server shut down cleanly.")

    except socket.error as error:
        print(f"Socket error: {error}")

if __name__ == "__main__":
    start_server()