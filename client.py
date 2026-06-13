import socket

HOST = "127.0.0.1"
PORT = 5050

def start_client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        print(f"Connected to server at {HOST}:{PORT}")
        print("Type messages to send. Type 'bye' to quit.")

        while True:
            message = input("Enter message: ")
            client_socket.sendall(message.encode())

            response = client_socket.recv(1024).decode()
            print(f"Server response: {response}")

            if message.lower() == "bye":
                break

        client_socket.close()
        print("Disconnected cleanly.")

    except ConnectionRefusedError:
        print("Error: Could not connect. Make sure the server is running first.")

    except socket.error as error:
        print(f"Socket error: {error}")

if __name__ == "__main__":
    start_client()