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
![[Pasted image 20240118104535.png]]