
# Script
- A script or scripting language is a computer language with several commands within a file capable of being executed without being compiled. Examples of server-side scripting languages include Perl, PHP (PHP: Hypertext Preprocessor), and Python. The best example of a client-side scripting language is JavaScript.
## Script installation 
- Some hacking tools are developed by some peoples and those peoples make it open-source, that means we can get those scripts/programs from GitHub. So we can download and use it. For this purpose git have a feature called ‘clone’
- Syntax
     ` git clone 'link_of_the_script_from_github' `
![[Pasted image 20240122112546.png]]

## Script module
- Scripts are made with scripting (programming) languages like(python, bash, go, ruby,...)
- So when we use these programming languages to do tasks their is something called modules/libraries these are needed to run the script as the dependencies.
**Example:**
1. Python: to install python modules we use `pip install 'module_name'` 
    - For requirements file -> `pip install -r requirements.txt`
    
2. Go: to install go modules -> `go install 'module_name'`

3. Ruby:  to install ruby modules -> `gem install 'module_name'`

## Python installation
- to install python module
`pip install term`
- if the pip command didn't work
`sudo apt inatall python3-pip`

## help commands on linux
1. **man (manual)**: ○This will give you the whole manual and instruction of a tool or command.
`man 'command'`

2. **help**
- Some Commands have help option.
    - 'command' -h
    - 'command' -help
    - 'command' - -help

# tr command
- The ‘tr’ in tr command stands for translation. This nifty command is used for translating one type of characters into another. For example, if you want to convert text into all upper cases .or all lower cases, tr command is what you can use.
`tr options 'char1' 'char2'`

| options |  | descrition | example |
| ---- | ---- | ---- | ---- |
| -c | --complement | replaces all characters that are not in char1 | echo 'linuxize' \| tr -c 'li' 'xy'   -> output= liyyyiyy |
| -d | --delete | delete characters specified in char1 | echo 'Linuxize' \| tr -d 'liz' -> output= Lnuxe |

# Linux Processes & Services
- As we interact with Linux, we create numbered instances of running programs called “processes”

| command |  |
| ---- | ---- |
| ps | for process running on my shell |
| ps -A | view all running process |
| ps -u | view users process |
| PID | Process ID |
### stop process
`Kill options PID`

| command  |  |
| ---- | ---- |
| kill -9 PID | to Stop a process immediately |
| kill -18 PID | to resume the process we stopped |
| kill -19 PID | to stop the process |
## Foreground / background
- when we  run commands at the prompt and waited for them to complete. We call this running in the “foreground.”
- we can Use the “**&**” operator, to run programs in the “background” or press **^z**
- To get the background process back to foreground `Fg`
- To stop a process going inside your shell just press `^C`

# Null devices
- /dev/null - Redirects output to nowhere.
- If you want to ignore output, you can send it to the null device, /dev/null. The null device is a special file that throws away whatever is fed to it. 
- You may hear people refer to it as the bit bucket. 
- If you do not want to see errors on your screen and you do not want to save them to a file, you can redirect them to /dev/null
- On shell output there are 2 things.
    - STDERR =  2
    - STDOUT  =  1
- to redirect the errors from a command result we do 
`command 2> filename`, here if you check the file you saved on it have errors only
- To redirect the error-FREE output
`command 1>filename`, 
- So if we redirect our commands output to /dev/null we will get error free result
`command 2> /dev/null`

# Symbolic linking
- Symbolic linking is same as Windows shortcut.
- it is a process of creating a linked shortcut form of file to some pre-existed file or folder.
**For example**: you can create program is some file and to create a shortcut format of that file you will use symbolic linking.
- ln is a command-line utility for creating links between files. By default, the ln command creates hard links. To create a symbolic link, use the -s (--symbolic) option.
- The ln command syntax for creating symbolic links is as follows:
`ln -s OPTIONS  FILE  LINK`
- Removing Symlinks
`unlink symlink_to_remove`

# alias
- Used to give a name to some bunch of commands.
**Example**: if i wanted to name ls -la  rex   so any time i want to get output of ls -la , just type `alias rex=’ls -la’`
- But this doesn’t work after you closed the terminal
- If you want to make it work, You will add it to your shell config file.
    - Bash = ~/.bashrc
    - Zsh = ~/.zshrc
    - Fish = ~/.config/fish/config.fish
    ![[Pasted image 20240122165654.png]]
# Tmux (Terminal Multiplexer)
- 