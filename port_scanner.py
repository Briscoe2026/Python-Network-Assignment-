import socket
from datetime import datetime
import time

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
            scanner.settimeout(1)
            result = scanner.connect_ex((host, port))

            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED")

            time.sleep(0.1)

    except socket.gaierror:
        print("Error: Invalid or unreachable host.")
    except socket.error as error:
        print(f"Socket error: {error}")

def main():
    print("Python Port Scanner")
    print("Only scan localhost or scanme.nmap.org")
    print(f"Scan started at: {datetime.now()}")

    host = input("Enter host to scan: ")

    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Error: Ports must be between 1 and 65535, and start must be less than end.")
            return

        print(f"\nScanning {host} from port {start_port} to {end_port}...\n")

        for port in range(start_port, end_port + 1):
            scan_port(host, port)

        print("\nScan complete.")
        print(f"Scan ended at: {datetime.now()}")

    except ValueError:
        print("Error: Please enter valid numbers for ports.")

if __name__ == "__main__":
    main()