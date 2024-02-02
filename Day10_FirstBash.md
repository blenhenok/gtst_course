# Bash script
- A bash script is a file containing a sequence of commands that are executed by the bash program line by line. It allows you to perform a series of actions, such as navigating to a specific directory, creating a folder, and launching a process using the command line.
- By saving these commands in a script, you can repeat the same sequence of steps multiple times and execute them by running the script.
- The term "shell" refers to a program that provides a command-line interface for interacting with an operating system. Bash (Bourne-Again Shell) is one of the most commonly used Unix/Linux shells and is the default shell in many Linux distributions.

- **if the default shell is not bash**
`echo "$0"`  => to check what kind of shell we are using
`chsh -s /bin.bash`   => to change to bash

## Script naming conventions
By naming convention, bash scripts end with `.sh`. However, bash scripts can run perfectly fine without the sh extension.
## Adding the Shebang
Bash scripts start with a `shebang`. Shebang is a combination of bash # and bang ! followed by the bash shell path. This is the first line of the script. Shebang tells the shell to execute it via bash shell. Shebang is simply an absolute path to the bash interpreter.
```bash
#!/bin/bash
```

## Creating our first bash script
- Our first script prompts the user to enter a path. In return, its contents will be listed.
- Create a file named `run_all.sh` using the `vi` command. You can use any editor of your choice.
```bash
vi run_all.sh
```

## Displaying (executing) bash script
- To make the script executable, assign execution rights to your user using this command:
```bash
chmod u+x 'file'
```
- Here,
    - `chmod` modifies the ownership of a file for the current user :`u`.
    - `+x` adds the execution rights to the current user. This means that the user who is the owner can now run the script.

- to display the output of the script:
    - **/bin/bash the_file.sh**
    - **./the_file.sh**   ->  need x
    - **the_file** -> need x

## Comments in bash scripting
- Comments start with a `#` in bash scripting. This means that any line that begins with a `#` is a comment and will be ignored by the interpreter.

# Variables and data types in Bash
- Variables let you store data. You can use variables to read, access, and manipulate data throughout your script.
- There are no data types in Bash. In Bash, a variable is capable of storing numeric values, individual characters, or strings of characters.
- In Bash, you can use and set the variable values in the following ways:
1. Assign the value directly:
```bash
country=Pakistan
```
2.  Assign the value based on the output obtained from a program or command, using command substitution. Note that `$` is required to access an existing variable's value.
```bash
same_country=$country
```
- This assigns the value of `country`to the new variable `same_country`

- ***Naming variables***
    - NO Space between the equal sign ( = )
        - NAME  =  “Nathan”   => ERROR
        - NAME=”Nathan”  =>  Correct.
    - Never Start with Numbers
    - USE double quotes only.

- *To use the variable we will use dollar sign( $ )  before the Variable name*
- *If you want to display the variable sticked with other text use ${VARIABLE_NAME}*
- Bash Variables are string by default.
**Example:**
```bash
#! /bin/bash

Name="nathan"
Sport="foot"
	echo "my name is #Name and i love playing ${Sport}ball"
```
`output => my name is nathan and i love playing football`

## system variables
- In Bash, system variables are predefined variables that are maintained by the shell itself. They define various aspects of the shell, such as the current user, the current working directory, and the system environment. You can use these variables in your Bash scripts to perform various tasks.
- Here are some examples of system variables in Bash:
    - *$HOME*: The home directory of the current user.
    - *$USER*: The username of the current user.
    - *$PWD*: The current working directory.
    - *$PATH*: The system path, which is a list of directories that the shell searches when you enter a command.
    - *$SHELL*: The path to the current shell executable.
- You can use these variables in your Bash scripts like this:
```
echo "The current user is: $USER"
echo "The current working directory is: $PWD"
```
- This will print the current user and working directory to the console.

## Arrays
- Arrays are lists or tuples on python.
- **Syntax:**
    - var=(“list1” “list2” “list3” “list4)
    - TO display echo: `${var[0]}`
    - To get all the elements: `${var[@]}`
    - To get the indexes: `${!var[@]}`
    - To get the length: `${#var[@]}`
    - To add element to the array: `var[4]=”list5”`
    - To remove from the array: `unset var[3]`
Example:
```bash
#! /bin/bash
a=('ubuntu' 'window' 'kali')

echo "${a[@]}"
unset a[2]
a[6]='mac'
echo "${a[@]}"
echo "${a[0]}"
echo "${!a[@]}"
echo "${#a[@]}"
```
```
#outputs:
ubuntu window kali
ubuntu window
ubuntu window mac
ubuntu
0 1 6
3
```

# Bash input
## Bash read
- Read used to accept inputs while the script is running.
- Syntax:
    - `read -p “Text To Display” var`
    - `read -sp “Password: ” var`  =>   used to accept hidden texts like password.
    - `read -a var`  =>   for accepting arrays(lists)
Example:
```bash
#! /bin/bash

read -p "Enter your name: " NAME
echo "your name is $NAME"
```

```
#output:

Enter your name: Nathan
your name is Nathan
```

## Argument
- These helps to get input before the script starts
- Syntax:
    - Just use $0-$9 while you want to work with the input
**Example**:
```bash
echo "your name is: $1"
echo "your father name is $2"
```

```/bin/bash hello.sh nathan hailu
your name is: nathan
your father name is hailu
```
# Bash sleep
- Sleep used to make a good waiting on our script.
- Syntax:
    - sleep 'number'
**Example:**
```
echo "my name is nathan"
sleep 2s
echo "my father name is hailu"
```
- this will make the second line wait for 2s before it starts to execute.

# Bash operation
- To do mathematical operations you have to do $(( expression ))
- we will use let keyword for assigning variable

- **Arithmetic Operations**
    - Addition `$(( a + b ))`
    - Subtraction `$(( a - b ))`
    - Multiplication `$(( a * b ))`
    - Division `$(( a / b ))`
    - Exponential `$(( a ** b ))`
    - Modulo `$(( a % b ))`
- **Assignment Operations **
    - Increment  “`let a+= i`”
    - Decrement  “` let a-= i`”
    - Multiply “ `let a*= i `“
    - Divide  “ `let  a/= i `“
- **Comparison operation** (Alphabetic comparison)
    - Greater Than =>  `-gt`
    - Less Than => `-lt`
    - Greater than and equals to => `-ge`
    - Less than and equals too  =>  `-le`
    - Equal  =>  `-eq`
    - Not equal  => `-ne`
- **Sign comparison**
    - >
    - <
    - >=
    - <=
    - =
    - !=

#if_statement
# Bash Conditional statements (if/else)
- On bash we don't have indentation so to finish writing the body you type “`fi`”
- If you used [ condition ]  => you will use alphabetic comparison
- If you used (( condition ))  => you will use numeric comparison
- *syntax:*
```bash
if [condition]  or ((condition))
then
body
else
body
fi
```

**Example:**
```bash
#!/bin/bash

echo "Please enter a number: "
read num

if [ $num -gt 0 ]; then
  echo "$num is positive"
elif [ $num -lt 0 ]; then
  echo "$num is negative"
else
  echo "$num is zero"
fi
```
- Script to determine if a number is positive, negative, or zero
- We can use logical operators such as 
    - AND `-a` 
    - OR `-o`

