# System Hacking
- System hacking is defined as the compromise between computer systems and software to access the target computer and steal or misuse their sensitive information. 
- The malware and the attacker identify and exploit the vulnerability of the computer system to gain unauthorized access.
- Here the malicious hacker exploits the weaknesses in a computer system to gain unauthorized access to its data or take illegal advantage.
## Linux system hacking
- As we all know, GNU/Linux is an Operating System (OS) assembled user the model of open-source software development and distribution and is based on Unix OS created by Linus Torvalds.
- Now to hack a Linux-based computer system and get access to a password protected Linux system, we have to know Linux's basic file structure. 
- As we know, Linux is considered to be the most secure OS to be hacked or cracked, but in the world of Hacking, nothing is 100% secured.
- Hackers usually use the following techniques to hack the linux system.
    - Hack Linux using the SHADOW file.
    - Another technique commonly used by hackers is to bypass the user password option in Linux.(Privilege Escalation)
    - In another technique, the hacker detects the bug on kernel and tries to take advantage of it.
## Window system hacking
- The user password of Windows OS, which appears after the Windows starts logging in, lets users protect the computer from getting unauthorized access.
- Choosing a strong password of more than eight digits is an excellent practice.
- Henceforth you can protect your files and folders from the hands of malicious users. 
- There are several tricks and techniques to crack a windows password. But, from the hacker's point of view, if you can use social engineer your victim and find a Windows computer open, you can easily modify the existing password and give a new password that will be unaware of the victim or the owner of the computer.
## Window login bypass


## Window pentest
- Windows is wider, than you think. As we learnt Linux systems you have to learn windows Systems too. 
- You have to learn PowerShell Scripting and usage.
- Managing Services, Users
- Active Directory system.
# shell
- A shell is a program that interprets our commands and gives the written commands to the Kernel.
- Based on Remote Access to the shell while Pentest, it is Classified into:
    - Bind Shell
    - Reverse Shell
## Bind Shell
- A bind shell opens up a new service on the target system, which the attacker connects to directly.
- The target system listens for a connection on a specific port.
- Once the attacker connects, they can execute commands on the target system.
- The attacker must know the target’s IP address.
## Reverse Shell
- A reverse shell, also known as a remote shell or “connect-back shell,” takes advantage of the target system's vulnerabilities to initiate a shell session and then access the victim's computer.
- A reverse shell causes the target system to connect back to the attacker’s system.
- The attacker’s system listens for a connection from the target.
- When the connection is made, the attacker has a shell session on the target system.
- The attacker does not need to know the target’s IP address.
# Netcat
- Netcat is a Command-line Interface (CLI) Based tool that is use to read/write data over TCP/UDP. 
- Netcat is designed to be a reliable back-end tool that can be used directly or easily driven by other programs and scripts.
- It’s a feature-rich network debugging and investigation tool, capable of creating almost any kind of connection its user might need.
- It is a tool That helps to create Reverse shells or Bind shells
- It is built in on kali and parrot but for windows you have to download it.
- Common Uses:
    - **Port Scanning**: Checking for open ports on a host.
    - **File Transfer**: Sending files over the network.
    - **Network Debugging**: Testing and troubleshooting network services.
    - **Chat**: Setting up a simple text-based chat system.
    - **Port Listening**: Opening ports to listen for incoming connections.