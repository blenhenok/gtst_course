# Introduction to linux
- linux is a kernel
- Kernel is a code/program that used to meet your Software and Hardware. And allocate some resources.
![](https://lh7-us.googleusercontent.com/fUju-G9b3G5bnYE837rfxC9MgokpMaBlOJy8xKYCM2bMUUaaaDPnUi7fEoZITkeAbg_9kLeFCRNOlF8cA8lMp6rdjJ9Kl4hiZkWE5jeRESolH7Rdxa0FTOjhJ8dnIJ5ea6GtL-vFb1TtT6xXpEYAEpp3DQ=s300)

## History of linux
- in1969 a team led by computer scientists Ken Thompson and Dennis Ritchie created the first version of UNIX on a PDP-7 mini computer.
- BUT IT WASN’T CHEAP AND OPEN-SOURCE
- Then Person called “LINUS TORVALDS” Created the Linux kernel. And posted it online to make it open-source.
- Richard Stallman announced the GNU project in 1983 and cofounded the Free Software Foundation in 1985.
- GNU is a free software replacement to the UNIX OS, But it was just software replacement not full OS {Examples: Bash, tar, emacs…} .
- So GNU + LINUX will give the GNU/Linux OS.
- *The GNU Linux project was started to create a Unix-like operating system created with source code that could be copied, modified, and redistributed*

# Shell
- Users communicate with the kernel by the shell.
- it is interface between the operating system and the user.
- The Shell is a Command Line Interpreter. It translates commands entered by the user and converts them into a language that is understood by the Kernel. and presents the output obtained after the execution of the task.
## Type of shell
- They differ in Colouring,Piping,command compilation, some kind of features.
- TO IDENTIFY YOUR SHELL “*echo $SHELL*”
1. **Bourne shell (sh)**: its the first shell to be introduced.
- it was not able to handle logical and arithmetic operations.
- it was less interactive and lack of comprehensive features.
- path name : /bin/ sh or /sbin/ sh
- prompt for the root user: #
- prompt for non-root user: $
2. **Korn shell (ksh)**: provide additional functionalities , has in-built support for arithmetic operations.
- path name : /bin/ ksh
- prompt for the root user: #
- prompt for non-root user: $
3. **Bourne again shell (bash)**: can be edited with the help of arrow keys of the keyboard.
- default shell for most linux and MacOS systems.
4. **Friendly interactive shell (fish)**: user friendly and simplicity.
- autosuggestions, web based configuration and advanced tab completion. 

# Operating system 
- it means the main software part of computer that helps to work on.
- It contains:
    - Kernel
    - application and system Software
    - Desktop environment
    - File extensions
    - Window manager

# Linux distributions / distro
- Distro is Modified Linux Kernels,type of operating systems with different:
    - linux kernel
    - packages (GNU)
    - package manager
    - desktop UI
- *some of the linux distros* 
- Debian
    - Kali linux
    - Ubuntu
    - Parrot
- Arch
    - Black arch
    - Garuda
- Fedora
- Red Hat
- Gentoo
- Android
![](https://lh7-us.googleusercontent.com/4lWJuc8D36YMhyaWj3hxvflZQQgHi8QhXYHlHngPbgzYHMPkYjX532ruu1t_p1Csgc_TuwsKDQ4aG8OE7YlncRrdq1EReivDAewuEuDrbywMI56Fpli4KS1msGqUXRtWRXfnB6jbsJ3YWZW7NNY8Mfz1_g=s2000)

1. ***kali-linux***: it is a Debian-derived Linux distribution designed for digital forensics and penetration testing. It is maintained and funded by Offensive Security.
Desktop enviroment : xfce
Package manager: apt
Shell: zsh
2. ***parrot OS***: it is a Linux distribution based on Debian with a focus on security, privacy, and development.
Desktop environment: mate
Package manager: apt
shell: bash
3. ***Garuda***: it is a Linux distribution based on the Arch Linux operating system.
Desktop environment: KDE plasma
Package Manager: pacman
shell: fish

## Do windows have distros?
- Windows is not open-source so peoples won’t use / edit it, so there won’t be other kind.
- It just give updates and adds some feature on it.