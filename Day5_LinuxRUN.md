## Advanced user commands
- To change password of user
    - *sudo passwd* 'username'
- To change user id
    - *sudo usermod  -u* 'new_id' 'username'
- To Delete User
    - *sudo userdel -r* 'username'
- To Change users on terminal
    - *su -* 'username'

## Sudors file
- The sudoers file is a file Linux and Unix administrators use to allocate system rights to system users
- The user you created doesn’t have power to use sudo as the original one. This is Because it is not Added in the sudoers file ( የSudoዎች file )
- To access this file
    - ***sudo visudo***

# Linux file permissions 
- Every file on linux have their own Owner and Permissions
- There is 5 main parts on the listing of files.
    - Permission
    - Owners
    - Date
    - Size
    - filename
![[fs.png]]

## File type
- Denotes the type of file. 
    - *d* means directory
    - *–* means regular file
    - *l* means a symbolic link
## Ownership
- it refers to who has access to the file
    - **user**: is the owner of the file, who usually creates it and mostly has full access
    - **group**: Every user is part of a certain group(s). A group consists of several users and this is one way to manage users in a multi-user environment.
    - **others**: anyone with access to the system belongs to this group.
- To change the owner of file you can use the command
    - *chown* user:group 'filename'
![[p.png]]

### chown command
- To change the ownership of a file

| commands | descriptions |
| ---- | ---- |
| chown 'new_user'  'file_name' | to change the user |
| chown 'new_user':'new_user_group'  'file' | to change both the user and group  |
| chown :'new_user_group'  'file'    | to change the user group |
| chgrp 'new_user_group'  'file' | to change the user gro |
## Permission
- Permissions for files
    - ***r*** (Read) – Can view or copy file contents
    - ***w*** (Write) – Can modify (add and delete) file content
    - ***x*** (Execute) – Can run(enter) the file (if its executable)
    - ***–***: No permission set

### chmod command
- used to change permission of files.
#### using chmod in absolute mode
- In the absolute mode, permissions are represented in numeric form (octal system to be precise). In this system, each file permission is represented by a number.
    - r (read) = 4
    - w (write) = 2
    - x (execute) = 1
    - – (no permission) = 0
- With these numeric values, you can combine them and thus one number can be used to represent the entire permission set.
![[pa.png]]

#### using chmod in symbolic mode
- The problem with the absolute mode is that you should always provide three numbers for all the three owners even if you want to change the  permission set for just one owner.
- In symbolic mode, owners are denoted with the following symbols:
    - u = user owner
    - g = group owner
    - o = other
    - a = all (user + group + other)
- The symbolic mode uses mathematical operators to perform the permission changes:
    - + for adding permissions
    - – for removing permissions
    - = for overriding existing permissions with new value
![[psy.png]]

### Advanced file permissions

