# Social engineering
- Social engineering refers to the manipulation of people into taking actions that compromise their security or privacy. It exploits human psychology and emotions rather than technical vulnerabilities.
- It applies to trickery or deception for the purpose of information gathering or computer system access; in most cases the attacker never comes face-to-face with the victim
### Why Social Engineering Works
- The purpose of social engineering is usually to secretly install spyware, other malicious software or to trick persons into handing over passwords and/or other sensitive financial or personal information
- Exploits human emotions (curiosity, fear, trust) and instincts.
- Targets cognitive biases (e.g., authority bias, urgency bias).
- Manipulates victims into taking actions that benefit the attacker.
# Types of social engineering 
- Based on how we do the social engineering attack, it is classified into many kinds.
## Phishing
- Phishing is tricking people into providing sensitive information, such as passwords or credit card numbers, by pretend to be someone one is not as a trustworthy source. 
- Scammers send deceptive emails or messages, pretending to be trusted entities (e.g., coworkers, banks, or government agencies). Victims may unknowingly share sensitive information or download malicious attachments.
- Phishing messages will usually contain a link that takes the user to a fake website that looks like the real thing. The user is then asked to enter personal information, such as their credit card number. This information is then used to steal the person’s identity or to make charges on their credit card.
- common types of phishing:
    - **Normal Phishing**: this is an attach that tries to fool any victim.
    - **Spear Phishing**: Is a an attack that is planned and made for some person with specific loving and mindset
- Phishing scams also come in a few different delivery forms:
    - **Email phishing** is one of the most traditional phishing methods and is often spam sent to many people at once.
    - **Shoulder surfing** is a physical technique used to obtain/get information by directly looking some ones computer screen/keypad. When we enter our password, we might say don't look at me that is shoulder surfing.
    - **Vishing (voice phishing)** is when a phisher calls or leaves a voicemail pretending to be from a trusted institution in hopes of gaining private information.
    - **Smishing (SMS phishing)** involves sending texts containing malicious links or probing for personal information.
    - **URL phishing** is when a phisher sends a link to a fake website that looks legitimate to the victim. When the victim clicks the link, they’re asked to provide private details that can be harvested by the attacker.
    - **In-session phishing** occurs when a victim is actively signed into an account or platform and a fake pop-up appears asking them to sign in again or to provide other sensitive information. It usually occurs on sites that don’t use https encryption.
    - **Dumpster Diving** Is a technique for getting data is a dumpsters or recycle bins. Old companies work was with papers, so when they finish with these papers whey will through them to the dumpster/basket. If hacker got that dumpster, and if those papers have some secret information, or company workers name with the Job they intended to do, it will make the attack wider.
## Pretexting 
- it is an attack in which the attacker creates a scenario to try and convince the victim to give up valuable information, such as a password.
- common pretexting attacks example:
    - **Romance scam**  is a type of social engineering attack that manipulates feelings like love. A scammer may pretend to be an online love interest in such a pretexting scam, taking weeks if not months to win the target’s confidence. Ultimately, they may ask for a large loan for an emergency, plane ticket, or a gift.
    - **Cryptocurrency scam** Hackers are tricking people interested in investing in cryptocurrency with pretexting scams by pretending to be wealthy and experienced investors.  After telling their targets tall tales of financial rewards, they convince them to “invest” in crypto with them. Once the scammers receive the money, they disappear.
    - **Whaling attack** Such hackers either pretend to be company leaders to target employees or directly target high-level players(CEO) in an organization.  Here, they may gain secret information or a sizable financial payment by using the pretext of a business deal.

# Social media hacking
- Social Medias are an online platforms That helps to connect and share moments and ideas. like Facebook, Instagram, Telegram, Twitter etc.
- To get the data from those highly secured social medias, we have to hack Directly the companies , but that is very difficult todo. 
- WHY is it difficult? Because
    - Their Security is Hard to broke
    - Their System is Safeguarded
    - Their Employees are Learnt
- So, to Hack those social media we need some vuln/weakest point, WHAT IS THE WEAKEST LINK?
    - **HUMAN BEINGS(HOSTS)**: Here, the vulnerability we got on those companies is The users/the host  so here we can use the social engineering attacks. 
    
# The Social Engineering Toolkit (setoolkit)
- The Social-Engineer Toolkit (SET) is a powerful open-source penetration testing framework specifically designed for social engineering. It allows you to perform advanced attacks against the human element in security assessments.
- It is pre-built on kali and parrot.
- To use: `sudo setoolkit` on linux terminal
- `exit` to quit the setoolkit
- Here are some of the most commonly used tools in the toolkit:
1. **Spear-phishing**: This tool allows you to send a phishing email that appears to be from a trusted source, such as a colleague or a company.
2. **Credential Harvester**: This tool allows you to create a fake login page for a popular website, such as Facebook or Gmail, and capture the victim’s credentials.
3. **Bypass Anti-virus**: This tool allows you to create a payload that bypasses anti-virus software.
4. **Infectious Media Generator**: This tool allows you to create a USB drive that automatically runs a payload when inserted into a victim’s computer.
### Launching a Phishing Attack with the Social Engineering Toolkit
- You can create a fake login page for a popular website, such as Facebook or Gmail, and capture the victim’s credentials.
- To create a fake login page using the SET, follow these steps:
1. Select “`1. Social-Engineering Attacks`” from the main menu.
2. Select “`2. Website Attack Vectors`” from the submenu.
3. Select “`3. Credential Harvester Attack Method`” from the submenu.
4. Enter the IP address of your system and the port number that you want to use.
5. Select the website that you want to create a fake login page.
6. Enter a name for your fake login page and select a template.
7. Once you have created your fake login page, you can send it to your victim by email, social media, or other means.
## Automations
- There are a lot of tools to do phishing. You can get them from github.
    - SocialPhish
    - Zphisher
- As you see you can have all of those social media hacked. But you may get some errors and confusions now because we haven’t seen about port forwarding. we will see in upcoming class
### How do we hack other websites
- Websites like telegram, they don't use username and password, they use phone number as login. 
- Here  we hack is the SMS code. To get this we can't just clone telegram, we just need to use social engineering.
- Some telegram hacking scenarios
    - Create a telegram support account and chat with them like they got a security breach and ask them to send the code we sent to you.(worked on 3 peoples)
    - Create a telegram bot based on what the user loves then, ask questions like for the registration you need phone number, then be quick and add the number to the telegram and when u are sure the SMS is sent for them, ask them to send the registration code we sent then BOOM!(worked on 4 peoples) 