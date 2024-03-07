# Network Hacking
- Network Hacking is gathering and exploiting of networks.
- The networks can be WAN or LAN.
- Network Hacking is an offensive branch of computer security related to networks hacking and the penetration of a target via the networking services or equipment. 
- This includes
    - Network information gathering
    - Sniffing
    - Network Attacks
## Network foot printing
- Network Hacking is generally means gathering information about domain by using tools
    - **Ping**: used for ping sweep 
    - **Traceroute**: It is used to trace out the route taken by the certain information. i.e. data packets from source to destination.
# Network sniffing 
- Sniffing is the process of monitoring and capturing all the packets passing through a given network using sniffing tools. It is a form of “tapping phone wires” and get to know about the conversation
## Types of sniffing 
####  Passive Sniffing
- the traffic is Visible but it is not altered in any way. Passive sniffing allows listening only. 
- It works with Hub devices. On a hub device, the traffic is sent to all the ports. In a network that uses hubs to connect systems, all hosts on the network can see the traffic. Therefore, an attacker can easily capture traffic going through.
- The good news is that hubs are almost obsolete nowadays. Most modern networks use switches. Hence, passive sniffing is no more effective.
#### Active Sniffing
-  the traffic is not only monitored, but it may also be altered in some way as determined by the attack. 
- it is used to sniff a switch-based network.
## Sniffing networks
- Let’s Sniff some networks. For this purpose we use a program called Wireshark.
# Wireshark
- Wireshark is a network packet analyzer. A network packet analyzer presents captured packet data in as much detail as possible.
- Wireshark technically is referred to as a “protocol analyzer”, but it uses only passive observation of network traffic. 
- Wireshark supports both live and offline analysis, has a graphical user interface, and can be used for analyzing multiple protocols 
- It is for windows and linux.
- Wireshark can capture traffic from many different network media types, including Ethernet, Wireless LAN, Bluetooth, USB, and more.
- It can Capture and record network Traffics and Save it in Form of cap/pcap file
- to get started
    - type `wireshark` in the terminal
    - search it on the applications
- After choosing a network interface, it will start capturing
- We can even see, what the user accessed/requested
## Tshark
- TShark is a network protocol analyzer. It lets you capture packet data from a live network, or read packets from a previously saved capture file, either printing a decoded form of those packets to the standard output or writing the packets to a file. TShark native capture file format is pcapng format, which is also the format used by Wireshark and various other tools.
- On the search bar you can search protocols(ICMP,ARP,HTTP..) or some ip addresses as shown. It also try to suggest you and complete it for you. 
### Unsecured connections
- To Demonstrate this Lets Use A service called FTP.
- If you need the cap/pcap : [pcap file](https://github.com/markofu/pcaps/blob/master/PracticalPacketAnalysis/ppa-capture-files/ftp.pcap) 
- If you do this it will collect all the un encrypted data and display for you

# ARP /Address Resolution Protocol/
- it is a network protocol used to find out the hardware (MAC) address of a device from an IP address. 
- It is used when a device wants to communicate with some other device on a local network (for example on an Ethernet network that requires physical addresses to be known before sending packets). 
- The reason why we need ARP is because computers need to know both the IP address and the MAC address of a destination before they can start network communication.
## ARP spoof
- ARP translates Internet Protocol (IP) addresses to a Media Access Control (MAC) address
- Most commonly, devices use ARP to contact the router or gateway that enables them to connect to the Internet.
- An ARP spoofing, also known as *ARP poisoning*, is a Man in the Middle (MitM) attack that allows attackers to intercept communication between network devices. The attack works as follows:
    - The attacker must have access to the network. They scan the network to determine the IP addresses of at least two devices⁠—let’s say these are a workstation and a router. 
    - The attacker uses a spoofing tool, to send out fake ARP responses. 
    - The fake responses advertise that the correct MAC address for both IP addresses, belonging to the router and workstation, is the attacker’s MAC address. This fools both router and workstation to connect to the attacker’s machine, instead of to each other.
    - The two devices update their ARP cache entries and from that point onwards, communicate with the attacker instead of directly with each other.
    - The attacker is now secretly in the middle of all communications
### Demo
- We will get the mac of our gateway
- We will get our linux machine mac: `arp -g`
- Enable ip forward: `sudo sysctl net.ipv4.ip_forward=1`
- Start the spoofing with arpspoof tool: `Arpspoof -i interface -t target -r defaultgatewayip`
- NOTE:   
    - ip of attacker: 192.168.1.8
    - Ip of victim: 192.168.1.3
    - gatewap : 192.168.1.1
## Demo in advance
- Install bettercap `sudo apt install bettercap`
- Start bettecap `sudo bettercap -iface wlan0`
- Scan the network
    - `net.probe on`
    - `net.show`  => to see the network
- Start arp spoofing
    - `set arp.spoof.targets 'ip'`
    - `arp.spoof on`
- Start Mitm
    - `net.sniff on`
    - `net.sniff off`
## Prevention
- Using static ARP tables: manually setted
- Switch security: some feature for ARP poisoning
- Encryption: not for arp but in case of leaks
# Mac flooding
- MAC Flooding is one of the most common network attacks. 
- Unlike other web attacks,  MAC Flooding is not a method of attacking any host machine in the network, but it is the method of attacking the network switches. However, the victim of the attack is a host computer in the network.
- the switches maintain a table structure called MAC Table. This MAC Table consists of individual MAC addresses of the host computers on the network which are connected to ports of the switch. This table allows the switches to direct the data out of the ports where the recipient is located.
- As we’ve already seen, the hubs broadcast the data to the entire network allowing the data to reach all hosts on the network but switches send the data to the specific machine(s) which the data is intended to be sent. This goal is achieved by the use of MAC tables. The aim of the MAC Flooding is to takedown this MAC Table. 
- In a typical MAC Flooding attack, the attacker sends Ethernet Frames in a huge number. When sending many Ethernet Frames to the switch, these frames will have various sender addresses. The intention of the attacker is consuming the memory of the switch that is used to store the MAC address table. 
- The MAC addresses of legitimate users will be pushed out of the MAC Table. Now the switch cannot deliver the incoming data to the destination system. So considerable number of incoming frames will be flooded at all ports.
- Macof will send a lot of fake MAC’s to the switch and makes if confused, and do stop proper functioning this can cause , disconnections between hosts.
- This can cause huge damage on the network, it is fixed by rebooting the router. DONT try it on your network
## Demo
- I have set ping sweep on my windows to check the connection `ping google.com -n 10000`
- Wireshark to see the package And used macof tool for the mac flood. `sudo macof -i wlan0`
- Also can be sent to specific 1 destination /ip `macof -i wlan0 -n 10 -d 192.168.220.140`
- The command needs sudo
## Prevention
- **Port Security** – Limits the no of MAC addresses connecting to a single port on the Switch. `switch port-security maximum 5`
- **MAC Filtering** – Limits the no of MAC addresses to a certain extent.


