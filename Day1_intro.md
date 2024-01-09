# general note
## git / GitHub 
- Git is a version control system or tool. Simply, a system to manage your files.
- Saves the file locally or remote server(GitHub / git lab)
- Made by the linux development community
- GitHub is a Web site/server which your git is hosted on. Your files will be saved in folder called “REPOSITORY”.
*For FIRST TIME*
- cd Desktop
- mkdir gtst && cd gtst
- git init - to initialize/ track a new file
- git config –-global user.name "Your username"
- git config –-global user.email "Your email"

*FOR NORMAL WORKS*
- git status - to see the status of files if the been committed or not
- git add .
- git commit -m ‘Your Comment’   
- git log - to check what we committed
    
*FOR GITHUB*
- git remote add origin 'repository URL'
- git push -u origin master
- git clone 'your project link'
    
# ETHICAL HACKING
## HACKING
- Hacking is referred to exploiting system vulnerabilities and compromising security controls to gain unauthorized access to the system.

- **Ethical hacking finds the weak points or loopholes in a computer, web application, or network and reports them to the organization.**
### Types of hackers on ethics
- ==black hat hackers==: most evil and with bad intention.
- ==white hat hackers==: the helping and with good intention.
- ==grey hat hackers==: in the middle, sometimes good, other times bad.

### Types of hackers on skill
- ==newbie / noob==: new and don't have much knowledge about hacking.
- ==script kiddie==: a relatively unskilled individual who uses scripts or programs developed by others, primarily for malicious purposes.
- ==hacker==: perfectly skilled, with small experience.
- ==elite/ pro hacker==: perfectly skilled, with experience.

## Why hacking happen?

ATTACK = MOTIVE(goal) + METHOD + VULNERABILITY 
- ==MOTIVE==: Information theft, manipulating data, Financial loss,Revenge, Ransom, Damaging Reputation.

## Elements of information security
***CIA triad*** 
- ==confidentiality==: data should be available to those with authorized access.
        - information is safe from accidental or intentional disclosure.
- ==integrity== : the information should be intact, complete and accurate.
        - information is safe from accidental or intentional modification or alteration. 
- ==availability== : the system or devices are ready to use as intended by the authorized person.
        - information is available to authorized user when needed.

## Skills needed to become a hacker
- programming
- linux
- networking
- system admin

## Phases of hacking
#### reconnaissance
- initial preparing phase by gathering information about the target.
        - passive : acquiring information without directly interacting with the target. ex.  using social media.
        - active : by acquiring the target directly. ex. via calls, emails or help desk.
#### scanning
- scanning the network by using the info we got earlier.
- by using tools like port scanners, network mappers and ping. 
#### gaining access
- the point where the hacker gets control or access.
#### maintaining access
- maintaining the access and control over the compromised system.
#### clearing tracks or logs
- the attacker must hide his identity by covering the tracks to continue the access to the system and remain un noticed 


# PENETRATION TESTING
- it is a method of evaluating the security of an information system or network by simulating an attack to find vulnerability, Security Measures, Documentation and Report Preparation
## Types of pen testing
- ==black box pen testing== : without prior knowledge about the system; test as attacker.
- ==white box pen testing== : with prior knowledge about the system; test as developer.
- ==grey box pen testing==: with limited knowledge; test as user.

# Terms
- **Red team**: are offensive and trying to attack, then report the way they got in.
- **Blue team** : are defensive people, who will do firewalls and try to protect the system.
- **Vulnerability assessment**: security check based on some list.
- **Security audit**: evaluation of an organization's security control and policies.
