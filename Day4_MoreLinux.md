# Linux file hierarchy 
- *File system is a directory structure that the OS uses.*
- Linux/UNIX have  a special file system than windows.

## system files
- System Files are files used by the system software( OS ).
- Windows: System files appear under the *local disk C:*
- Linux: System files appear under the *root directory ( / )*

# File structure in detail

1. ***/*** ( root )
- Every single file and directory starts from the root directory
- The only root user has the right to write under this directory
- /root is the root user’s home directory, which is not the same as /

2. ***/bin*** (binary executables)
- store binaries required for execution of different commands and programs in linux.
- it serves as the storage location for important commands and programs.
- it ensures that these executables are easily accessible for the user.

3. ***/boot*** (boot loader files)
- contains all needed files for boot process. like
    - configuration files
    - system map files
    - linux kernel files
    - initial RAM files

4. ***/dev*** (device files)
- contains the special device files for all devices like USB or any device attached to the system.

5. ***/etc***  (et cetera)
- Contains configuration files required by all programs.
- This also contains startup and shutdown shell scripts used to start/stop individual programs.

6. ***/home*** (home directory)
- default path for all users to store their personal files.

7. ***/lib*** (library)
- contain shared library images needed to boot the system and run command in the root file system i.e. by binaries /bin and /sbin.

8. ***/media***
- Temporary mount directory for removable devices; such as CD-ROMs.

9. ***/mnt***
- it contains Temporary mount directory where system admins can mount filesystems.

10. ***/sbin*** (system binaries)
- Just like /bin, /sbin also contains binary executables.
- The linux commands located under this directory are used typically by system administrator, for system maintenance purpose.

11. ***/tmp*** (Temporary Files)
- Directory that contains temporary files created by system and users.
- Files under this directory are deleted when system is rebooted.

12. ***/usr*** (User Utilities)
-  Contains binaries, libraries, documentation, and source-code for second level programs.
- /usr/bin contains binary files for user programs. If you can’t find a user binary under /bin, look under /usr/bin. For example: at, awk, cc, less, scp
- /usr/sbin contains binary files for system administrators. If you can’t find a system binary under /sbin, look under /usr/sbin. For example: atd, cron, sshd, useradd, userdel/usr/lib contains libraries for /usr/bin and /usr/sbin
- /usr/src holds the Linux kernel sources, header-files and documentation.


# Text editors
- Programs That used for text processing.
- Linux command line text editors
    - VIM
    - Nano
    - Emacs
    - Neovim
- Linux Graphical Text editors
    - Sublime
    - Vs code
    - Gedit
    - Pluma

## VIM
- Before vi the primary editor used on Unix was the line editor User was able to see/edit only one line of the text at a time
- Then then vi editor improved and developed VIM. ( VI iMproved)
- The vim editor is:
    - a very powerful
    - but at the same time it is cryptic
    - It is hard to learn, specially for windows users
- It have mainly to modes
    - Command mode -> where you can do commands
    - Input mode -> where you can write

- *syntax*  ->  vim 'file name'

| commands | description |
| ---- | ---- |
| i | insert text |
| esc | to get back to command mode |
| :w | save |
| :q | quit |
| :wq! | save and quit |
| :u | undo |
| %!'command' | to execute commands |

## Nano
- This text editor is a user-friendly, free and open-source text editor that usually comes pre-installed in modern Linux systems.

- *syntax* -> nano 'filename'
- then start typing

| commands | description |
| ---- | ---- |
| ctrl + s | save |
| ctrl+ x | exit |
| ctrl + t | execute |
| ctrl + g | help |
| ctrl + k | cut |
| ctrl + r | read file |
| alt + u | undo |
| alt + e | redo |
- ctrl + r = used to append text from other files; we need to specify the path.

# Linux user management
- On Computer system, person who uses the computer is called “user”. Every Users have Group. Users have their own file & applications.
- To know our name on linux -> “ *whoami* “
- Those users have power/privilege. On linux  there's 2 kinds users.
    - Root  id = 0
    - Normal User id start with 1-999
- The root user have the power to do everything on linux. 
- but if users want to have a root access they add sudo in front of the command .

 ***sudo Command***
- SUDO = Superuser do  ,  used to pass permission denied

## Creating users
- On linux, to create users you can use the following commands
    - Useradd -> simple, sudo useradd username
    - Adduser   -> Detailed, sudo adduser username
- The User files are stored inside **/etc/passwd**
- The User password are stored inside **/etc/shadow**
- When you create a user it creates a group with that name.

[[Day5_LinuxRUN]]