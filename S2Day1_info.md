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
    - whois (`sudo apt install whois`)
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
# personal information
- The information we gather about a Persons are
    - Full Name
    - Address(Physical Address, All Social Media Address, Phone address)
    - What the person loves
    - Friends
    - Status
- Persons information can be gathered by active and passive.
- gathering and Analyzing Different Information Based on Public resource is called *OSINT* ( Open Source Intelligence).

- **Getting name by phone number**: https://www.truecaller.com/
- **Social media address**: search engines(google, Bing, yahoo)
- **IP geolocation**: If you got the private Ip address of someone you can insert it to https://www.iplocation.net 
# Applications / Software
- The information we gather about a Applications are
    - Which programming language used
    - Which framework used
    - Source codes
    - Their logic and Function
# Reverse image search
- Reverse image search is a technique of searching with images.
- Ex: think like user posted a picture with a background of some area, if the user didnt talk about the place we can just search the image and the search engines will give as some similar photos where they are taken in same place(not 100% accurate) 
- We can use:
    - https://tineye.com/
    - https://www.labnol.org/reverse/
    - https://images.google.com/ 

# Goggle docking (google hacking database)
- it's not hacking into Google servers!
- Google hacking is using different Google operators to effectively optimize search results.
- It also involves using Google to identify vulnerabilities in websites.
- Results are highly customizable.
- THIS IS THE MOST POWERFUL SKILL OF HACKER!
## Basic operators
- don't add space between the sign and the word
1. **Inclusion of something common (+)**: EX: `nathan hailu +geeztech +ceo`
2. **Excluding terms(-)**: EX: `antivirus -software`
3. **Search for the exact term(" ")**: EX: `"how to eat food"`
4. **Placeholder( * )**: EX: `parlament votes on the * bill`
5. **Boolean OR ( | )**: EX: `"nathanhailu" | "nathan hailu"`
## Advanced operators
- These are Syntaxes used by Google.	
1. **intitle**: Google returns results with the word/phrase found within the title of the page
Example: intitle:index.of, intitle:”Hackers Bible”
2. **inurl** : Finds a specific term within the URL
Example: inurl:view/index.shtml
3. **filetype**: Searches for a specific filetype
Example: “Hacking” filetype:pdf, filetype:txt
4. **Intext**: Google returns links that contains Texts from that link
Example: intext:”Hackers in Ethiopia”
## Mixing operators
**Example**:
- intitle:admin intitle:login
- "mysql dump" filetype:sql intext:password
- inurl:securethiscompany.com intitle:index.of
## Further on google docking
- Further on google docking
https://www.exploit-db.com/google-hacking-database 
- If you do a lot of dockings with same ip address, Google will block you for some hours.
