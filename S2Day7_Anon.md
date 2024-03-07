# Anonymity 
- Anonymity encompasses the quality or state of being unknown to most people.
- When Black Hat Hackers do Security tests on some target, They will be unknown. This is because they are doing illegal things so they try to be anonymous.
- Keeping your identity private, but not your actions. 
- Anonymity is Simply using a fake Profile/Location/Identity/personality
## Online privacy
- **incognito/privacy tabs**: These Programs are simply not logging what we are doing(aka history, cache, cookie) but still the site we visit with this program will have our ip and other information also our ISP/internet service provider/ will know. 
- Therefore, they don't give as real privacy. So how can we get that?
## Methods of anonymity
- There are several ways to be protected or to be Anonymous on the internet. 
- These methods can change our identity, location or personality.
    - Proxychains
    - Tor Network
    - VPN
    - Mac change
    - Incognito
    - Secured OS
    - Temp mail
    - Temp number
# Proxy server
- A proxy server acts as an intermediary between a client (such as your computer) and a resource server (such as a website).
- When you request a resource (like a web page), your device sends the request to the proxy server instead of directly to the resource server.
- Getting Working Free Proxy Server is hard, But Hackers Most of the time Buy Some VIP servers, so they can do anything what they want.
- **Find some Proxy servers to use**.
    - google.com
    - https://geonode.com/
- **open** `/etc/proxychains4.conf`on the terminal
    - Turn on any kind proxychain you need
    - Put your proxy servers
```sh
# 
[proxylist]
#add proxy here ..
http 117.160.250.163 82
http 218.201.71.75 8060
http 43.255.223.232 83
http 120.37.121.209 9091
# default set to 'tor'
socks4 127.0.0.1 90.50
```
- **Accessing with proxy chains**
    - Add “proxychains” in front of any command: `proxychains nmap scanme.nmap.org` , `proxychains curl ifconfig.me`
## Proxy chains
- Proxy chaining is a technique that links several proxy servers together to enhance online privacy and security.
- - Proxy chaining involves passing internet traffic through a series of proxy servers, **masking the original IP address**.
## Types of proxy chains
- Based on the path we follow There are 4 Types of proxy chains.
1. **Dynamic Chain**:
    - In a dynamic chain, the proxy servers are selected dynamically for each request.
    - The order and number of proxies can vary, providing flexibility.
    - This approach ensures that no fixed pattern is followed, making it harder to trace back requests.
    - If there is any server that is not working it will be skipped. 
    - If any of them doesn’t work it will be broken and display errors.
2. **Strict Chain**:
    - A strict chain involves a fixed sequence of proxies.
    - While it offers predictability, it lacks the flexibility of dynamic chaining.
    - All Proxies chained in the order as the are listed.
    - All proxies Have to be up and working, if one server is not working it will display error
3. **Round Robin Chain**:
    - In a round robin chain, requests rotate through a predefined list of proxies.
    - Each request uses the next proxy in the sequence.
    - It will skip if 1 proxy is not working
    - If all the proxies not working it will start again and check them. This makes it different from Dynamic chain.
4. **Random Chain**:
    - A random chain selects proxies randomly for each request.
    - It adds an element of unpredictability, making it challenging for anyone monitoring the network.
    - Not working will be Skipped!
    - Each Request will be in random sequence of servers
# T.O.R/The Onion Routing/ Network
- Tor is an open-source privacy network that enables anonymous web browsing.
- The worldwide Tor computer network uses secure, encrypted protocols to ensure that users' online privacy is protected. 
- Tor users' digital data and communications are shielded using a layered approach that resembles the nested layers of an onion.
- Tor uses an onion-style routing technique for transmitting data. 
- When you use the Tor browser to digitally communicate or access a website, the Tor network does not directly connect your computer to that website. 
- Instead, the traffic from your browser is intercepted by Tor and bounced to a random number of other Tor users’ computers before passing the request to its final website destination. 
## Torghost
- Clone it from github: https://github.com/SusmithKrishnan/torghost
- Install  tor: `sudo apt install tor`
- go to torghost: `cd torghost`
- install torghost: `sudo python3 torghost.py`
- start: `sudo python3 torghost.py --start`
- **Your last Proxy IP will be shown(Public IP)**
- stop : `sudo python3 torghost.py --stop`
# VPN / Virtual Private Network /
- A VPN establishes a secure, encrypted connection between your computer and the internet, providing a private tunnel for your data and communications while you use public networks.
- There are a lot of VPNS, those are paid and free
- The paid are more secured and private, still the free are Good
- **Example**: Nord VPN, Proton VPN, windscribe VPN,...
## Types of VPNs
#### Site-to-Site VPNs
-  Site-to-site VPNs enable organizations to combine their networks from different locations into a single network (called an intranet).
- allowing multiple locations to communicate over the Internet as if they were local.
- Router + Routers
#### Remote Access VPNs
- These VPNs allow remote users (such as employees) to access their company’s private network from outside the office.
- involves the client's computer creating a virtual interface that behaves as if it is on a client's network
- Hacking game utilizes **OpenVPN**, which makes a TUN Adapter letting us access the labs
- When analyzing these VPNs, an important piece to consider is the routing table that is created when joining the VPN.
- If the VPN only creates routes for specific networks (ex: 10.10.10.0/24), this is called a **Split-Tunnel VPN**, meaning the Internet connection is not going out of the VPN. 
- This is great for Hacking Games because it provides access to the Lab without the privacy concern of monitoring your internet connection.
#### SSL VPNs
- essentially a VPN that is done within our web browser and is becoming increasingly common as web browsers are becoming capable of doing anything.
- These will stream applications or entire desktop sessions to your web browser.
# Mac changer
- As We saw MAC address can tell about our Device. So , if we changed that we can change our device id.
- We can use tool called “macchanger” on kali: `sudo macchanger -r wlan0`
- 1st turn off the interface you want to change.: `sudo ifconfig wlan0 down`
- Turn it on now! `sudo ifconfig wlan0 up`
- You can add your specific MAC with -m option: `sudo macchanger -m 'specific mac' wlan0`
# Incognito mode
- This is a mode that browsers have.
- This will help you to have a browser with out logging your history, cookies, cache,.. 
- This will help you when you are try to surf some site but if you don't need the site to know your identity, you can use this because it doesn't have any recording process.
# Secure OS
- This are Operating systems, that have a security and privacy feature. Windows and Mac 
- OS will record some of your activity also they are not good on privacy and security. 
- Therefore  Linux OS is always recommended when you think about privacy and Security.
# Temporary mail
- While You do some pentest you don't have to expose your email and profile for this purpose you need fake emails, 
- but if you don't have to time create one you can use fake email providers. 
- https://temp-mail.org/
- It have a browser extension too 
## True anonymity is HARD
- Every server you connect to on the internet be it a web server, a mail server, or a VPN server can see your IP address. This is a number that uniquely identifies your internet connection and can be easily traced back to you. 
- Achieving true anonymity on the internet therefore requires good operational security (OPSEC) on your part to ensure your real IP address is not revealed.
- Tools that can hide your IP address and protect anonymity include VPNs and the Tor anonymity network, but there’s no solution that can guarantee 100% anonymity. 
- Tor is sometimes considered to be more anonymous than VPNs due to its decentralized nature, but it comes at the cost of lower performance, ease of use, and stability.
- Full anonymity is difficult because you must always use anonymity tools for all aspects of your online life, as even a temporary lack of anonymity is sufficient to expose your identity.
# Deep web
- The deep web refers to all the web pages and data that are not indexed by search engines and cannot be accessed through traditional search methods. It includes content that is protected by passwords, databases, and other security measures. 
- Examples of deep web content include private email accounts, online banking portals, subscription-based websites, and more. 
- Essentially, the deep web is the part of the internet that is not easily accessible to the general public.
# Dark Web
- The dark web is a part of the internet that isn't indexed by search engines. 
- The dark web is a small portion of the deep web that is intentionally hidden and requires specific software or configurations to access.
- Their link ends with .onion , this is because it uses TOR networks. Also this kinds of links won’t be opened by normal browser. 
- For this purpose we need a special .onion reading browser, *Example: Tor browser*.
- You can buy credit card numbers, all manner of drugs, guns, counterfeit money, stolen subscription credentials, hacked Netflix accounts and software that helps you break into other people’s computers. You can hire hackers to attack computers for you. You can buy usernames and passwords.
- Also there are emailing service sites and normal Facebook too(but more secured).
- As you see This side of internet is little bit dangerous because a lot of evil hackers are there. For this purpose we have to change our identity, so we use Anonymity.
- There are Specific OS that are planned and Made for dark web access. Like:
    - Tails OS
    - Whonix OS
    - Qube OS
 ### Tor browser
- to install : `sudo apt install torbrowser-launcher`
# DOS and DDOS Attacks
- **DoS** is short for Denial-of-Service attacks. 
- **DDoS** stands for Distributed Denial-of-Service attack.
- It's used to crash a website by overwhelming the network with access requests from a computer. This method also crashes a targeted website and makes it unavailable to legitimate users.(like Mac spoofing)
- On DDOS, the request will be sent from Different Computers/hosts this will make the attack harder.
- IT is Highly illegal!
- Techniques:
    - SYN floods: Sending lots of SYN
    - Service Request floods: Create many connections
    - Application level DOS: Exploiting vulns like
        - Buffer Overflow
        - SQL injection
## Tools for DOS
- SolarWinds Security Event Manager (SEM)
- ManageEngine Log360
- HULK
- Tor’s Hammer
- Slowloris
- LOIC
- Xoic
- DDOSIM
- RUDY
- PyLoris
## Prevention
- Have you seen Cloudflare, These pages are One of the prevention ways.
- Limit or shut off broadcast forwarding where possible
- Set up firewalls
- Eliminate and patch known vulnerabilities
- Monitor network inbound traffic


