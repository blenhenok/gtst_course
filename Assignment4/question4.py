import socket

def get_network_info():
    hostname = socket.gethostname()
    gateway_ip = socket.gethostbyname(hostname)
    ip_class = gateway_ip.split(".")[0]
    print(f"Gateway IP: {gateway_ip}")
    print(f"IP Class: Class {ip_class}")

if __name__ == "__main__":
    get_network_info()
