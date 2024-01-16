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
- contains the special device files foe all devices like USB or any device attached to the system.

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
- it contains Temporary mount directory where sysadmins can mount filesystems.