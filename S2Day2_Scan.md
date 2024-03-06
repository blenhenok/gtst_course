# Scanning and Enumeration
- It is the step which helps to test a system based on the information we gathered. it refers to the package of techniques or procedures used to identify hosts, ports, and various services within a system
### Why we do scanning
- It helps to Identify HOST’s System detail
    - Operation System
    - Service versions
- To Discover Open Ports
- To Discover Live Systems

## Network scanning
- There are Many kinds of scanning methods and tools for different purpose.
    - **For Network mainly**: NMAP, netdiscovery
    - **For Subdomain**: Sublist3r,subfinder,amass
    - **For website**: Nuclei , Nessus, Acunitix
# Nmap (network mapper)
- It is used to scan Network, Ports, OS etc. It is made for windows and linux
- ON kali linux it is built in.
- To check the existence of nmap on your system: `nmap --version` 
### Live system discovery
- Discovering live system means, Checking up and running hosts(clients/servers) on a network.
- We have seen Host checking last time with ping  sweep method.(getting Ip with link)
### Ping sweep
- This is a method of checking if host is up or down.
- A ping sweep involves sending multiple ICMP (Internet Control Message Protocol) packets (commonly known as “pings”) to a range of IP addresses.
- Each IP address represents a potential host on the network.
- If a host is active and healthy, it responds with an ICMP ECHO reply.
- syntax: `ping 'ip address'`
- From echo requests we can gather the following information
    - OS type: Windows (32 byte), ttl=108 or Linux (64 byte), ttl=64
    - Connection stability: Time 
- Ttl : time to live
## Nmap ping sweep
- Nmap can perform ping sweep too.
- Syntax:  `nmap -sn 'IP address'`  
- -sn = no port scan
- The simplest way to ping sweep multiple hosts is to append them one by one as shown:
    - `nmap -sn [ip 1] [ip 2] [ip 3]`
- Ping sweep the entire subnet with the nmap command: you can use the wildcard `*` replacing the last octet (the last part of your IP after the `.`:
    - **Example** : `nmap -sn 198.68.12.1.*`
-  Ping sweep multiple hosts by specifying the IP range:  if you want to check whether the IPs in a specific range are up or not, you can benefit from this method.
    - **Example**:  let's say I want to check IPs from `192.168.1.1` to `192.168.1.10` then I will be using the following: `nmap -sn 192.168.1.1-10`
#### Warning
- Doing ping sweep is not undetectable thing. You are trying to ping a specific ip, And trying to do security pentest on my system.  it can be seen on the ip request of the host system.
- Some Organizations or system admins, will block any ICMP requests. Here the ping sweep wont work, and when you try this it says “host is down” but it is not To make it work we just escape the some option
    - Syntax:  `nmap -Pn 'IP address'`
    - -Pn : no ping
    - This method will Jump host discovery because it will take the ip as Up and try to do port discoveries.
## Port
- Port is process-specific or an application-specific software construct serving as a communication endpoint, which is used by the Transport Layer protocols of Internet Protocol suite, such as User Datagram Protocol (UDP) and Transmission Control Protocol (TCP)
- It is like a door for some purpose/service
-  Each port is associated with a specific process or service.
- Ports allow computers to differentiate between different kinds of traffic:
    - For example, emails go to a different port than webpages, even though both reach a computer over the same Internet connection.
- On computer there are different 65,536 ports with different job(like the window and door). 1-1024 = reserved(well known) ports
- **Example**:
    - **Ports 20 and 21:** FTP, File Transfer Protocol transfers files between a client and a serve and uses port numbers 20 & 21.
    - **Network Port 22:** The Protocol Secure Shell (SSH) creates secure network connections.
    - **Port 25:** For Email, use Simple Mail Transfer Protocol (SMTP).
    - **A Port 80:** Hypertext Transfer Protocol (HTTP) is the protocol that makes the World Wide Web possible.
    - **Port 123:** Network Time Protocol (NTP) allows computer clocks to sync. This process is essential for encryption.
    - **Port 443:** HTTP Secure (HTTPS) is the secure and encrypted version of HTTP. All HTTPS web traffic goes to port 443.
### Port status
- Ports can be on different status
    - **Open ports**: are ports open for accepting any requests, is accessible for communication.
    - **Closed ports**: are ports which are not accepting any request but there is some service running on it.
    - **Filtered ports**: These are ports which nmap is not sure of being open or closed. Network obstacle (firewall, filter) blocking the port, and its status (open or closed) cannot be determined directly.
### Open port discovery
- On some system ports can be open for some purpose
- Example: anywhere when you access websites there is web port open(80,443), If you are getting some shell activity there is port 22 open
- there problem, is there are some ports open without intention, this leads to attack
- We can use nmap to check which port is open/closed And this is called **port discovery**
- Syntax:
    - `nmap IP`    =>    only the 1000 ports
    - `nmap -p port 1,port2,port3 IP`     =>    only    port 1,2,3
    - `nmap -p- IP`     =>  All the 65K port
- We can use Another Trick with **netcat**
    - `nc -nv 'ip address' 'port'` 

# Scanning methods
- Nmap scans network in different modes
    - TCP connect (TCP scan)
    - TCP SYN (Stealth scan)
    - UDP scan
    - Xmas scan
### TCP scan 
- An adversary uses full TCP connection attempts to determine if a port is open on the target system.
- The scanning process involves completing a three-way handshake with a remote port. If the full handshake cannot be established, the port is reported as closed.
- the three-way handshake:
    - **SYN** (synchronize): The client initiates the connection by sending a segment by sending SYN flag.
    - **SYN + ACK** (acknowledgment): the server responds to the clients request. The ACK signifies the response to the segment received, and the SYN indicates the sequence number the server will use for its segments.
    - **ACK**: In the final part of the handshake, the client acknowledges the server’s response. Both sides establish a reliable connection, and subsequent data transfer can begin.
- TCP scan works like this, so nmap will send the SYN request to the ports and if they reply with SYN/ACK nmap will reply with ACK BOOM!!! That port is open!! Else the port is closed/filtered.
- Syntax: `nmap -sT 'IP address'`


