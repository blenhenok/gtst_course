import socket

def scan_ports(target, ports):
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout for the connection attempt
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
        except KeyboardInterrupt:
            print("\nExiting due to user interruption.")
            break
        except socket.gaierror:
            print("Hostname could not be resolved. Exiting.")
            break
        except socket.error:
            print("Could not connect to server. Exiting.")
            break

if __name__ == "__main__":
    target_host = input("Enter the target hostname or IP address: ")
    target_ports = [80, 443, 22, 8080]  # Example ports to scan
    scan_ports(target_host, target_ports)
