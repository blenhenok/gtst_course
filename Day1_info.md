# Reconnaissance (Information Gathering)

## Foot printing
- Foot printing is a specific phase within reconnaissance.
- It focuses on collecting detailed and specific information about a target’s: Network infrastructure, System architecture, IP addresses.
- The aim of foot printing is to create a detailed profile of the target’s network structure, which can be useful for planning further stages of an ethical hacking engagement
FOOTPRINTING = FOOTSTEP + PRINTING(LOGGING)

## Why do we need recon
- To Get access on system 1st you have to know the system. Knowing the system will lead you to know if the system is vulnerable

## Types of information gathering(foot printing)

### Passive foot printing
- Involves gathering information from publicly available sources such as websites, news articles, and company profiles.
### Active foot printing
- This kind is when we try to gather information directly by contacting that person.
**Example:**
    - When you go to the bank and ask for some information.
    - Chatting with person on social media to know about them.
- Doing Active Foot printing without permission is ILLEGAL!! 
- Utilizes more intrusive methods to access sensitive data, such as hacking into systems or applying social engineering techniques. The choice of approach depends on the desired information and the level of access to the target.

# Websites
- the information we can gather about websites are
    - IP Addresses
    - Development frameworks(Technologies used and versions)
    - Name
    - DNS information
    - Subdomains, Assets, Contents

## Ip addresses
- Active recon(on our terminal)
    - `ping 'website link'`
    - `nslookup 'website link'`
    - `host 'website link'`
- Passive recon(www.nslookup.io)

## Development frameworks
- Use simple browser extension 
    - Wapplyzer
    - Builtwith
- Terminal tool
    - whatweb(sudo apt install whatweb)- `whatweb 'website link'`

## DNS information
- For this you can use whois terminal +website tool
    - whois (sudo apt install whois)
    - `dig 'website link'`

# computers/ phones
- The information we gather about a Computers/Hosts are
    - IP Addresses
    - OS information
    - Host Name
    - MAC address
    - Open services or ports

# Networks
- The information we gather about a Networks are
    - IP Addresses
    - Ports, Services
    - Class and Type of Network
    - Subnets 
    - Hosts on that Network
    - Strength and security of that Network
