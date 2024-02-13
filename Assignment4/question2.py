import nmap

def nmap_port_scan(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments="-p 80,443,22,8080")  # Example ports to scan
    for host in nm.all_hosts():
        for port in nm[host]["tcp"]:
            state = nm[host]["tcp"][port]["state"]
            print(f"Port {port} on {host} is {state}")

if __name__ == "__main__":
    target_host = input("Enter the target hostname or IP address: ")
    nmap_port_scan(target_host)
