# Regular expression /regex/
- most filter validation for any platform are done by regex.
- Regex is PATTERN!
- it are used on linux tools called grep, awk and sed.

#email_regex: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

# Regex functionality in Python
- The `re` module in Python provides support for regular expressions. Here is an example of how to use regular expressions in Python:
```
import re

# Define a pattern to match
pattern = r"hello"

# Define a string to search
string = "Hello, World!"

# Search for the pattern in the string
match = re.search(pattern, string)

# Print the result
if match:
    print("Match found!")
else:
    print("Match not found.")
```
- `re.search(<regex>, <string>)` scans `<string>` looking for the first location where the pattern `<regex>` matches. If a match is found, then `re.search()` returns a match object. Otherwise, it returns [`None`.

## Metacharacters in regex

### Repeaters ( * , + and {})
- These symbols act as repeaters and tell the computer that the preceding character is to be used for more than just one time.
1. **The asterisk symbol ( * )**: It tells the computer to match the preceding character (or set of characters) for 0 or more times (up to infinite). *0++*
**Example :** The regular expression ab* c will give  ac, abc, abbc, abbbc….and so on 

 2. **The Plus symbol ( + )** :It tells the computer to repeat the preceding character (or set of characters) at at least one or more times(up to infinite). *1++*
**Example :** The regular expression ab+c will give abc, abbc, abbc, … and so on.

3. **The curly braces { … }** : It tells the computer to repeat the preceding character (or set of characters) for as many times as the value inside this bracket. *{a,b}*
**Example :** {min, max} means that the preceding character is repeated at least min & at most max times.

### Wildcard ( . )
- The dot symbol can take the place of any other symbol, that is why it is called the wildcard character.
- Used to get All the line except new lines
**Example :** The Regular expression .* will tell the computer that any character can be used any number of times.

###  The caret ( ^ ) 
- The caret symbol tells the computer that the match must start at the beginning of the string or line.
```
>>> re.search('^foo', 'foobar')
Match object; span=(0, 3), match='foo'>
>>> print(re.search('^foo', 'barfoo'))
None
```

### The dollar ( $ ) 
- It tells the computer that the match must occur at the end of the string or before \n at the end of the line or string.
```
>>> re.search('foo$', 'foobar')
None
>>> print(re.search('^foo', 'barfoo'))
Match object; span=(0, 3), match='foo'
```

### Optional character ( ? )
this is similar to `*` and `+`, but in this case there’s only a match if the preceding regex occurs once or not at all. *(0,1)*
```
>>> re.search('foo-?bar', 'foobar')                     # Zero dashes
Match object; span=(0, 6), match='foobar'>
>>> re.search('foo-?bar', 'foo-bar')                    # One dash
Match object; span=(0, 7), match='foo-bar'>
>>> print(re.search('foo-?bar', 'foo--bar'))            # Two dashes
None

```

### Character Classes
- A character class matches any one of a set of characters. It is used to match the most basic element of a language like a letter, a digit, a space, a symbol, etc. 

 `\s`: matches any whitespace characters such as space and tab.  
 `\S`: matches any non-whitespace characters.  
`\d` : matches any digit character.  
`\D`: matches any non-digit characters.  
`\w` : matches any word character (basically alpha-numeric)  
`\W`: matches any non-word character.  
`\b`: matches any word boundary, include spaces, dashes, commas, semi-colons, etc.

### pipe ( | )
- used to specify or search multiple patterns. like, `P1|P2`
**Example :**  th(e|is|at) will match words - the, this and that.
```
>>> re.search('foo|bar|baz', 'bar')
Match object; span=(0, 3), match='bar'>
>>> re.search('foo|bar|baz', 'baz')
Match object; span=(0, 3), match='baz'>
>>> print(re.search('foo|bar|baz', 'quux'))
None
```

### Escape (`\` )
- Used to search symbols that are metacharacters.
*Syntax*:`  \sign`
```
import re

str1 = "Emma is a Python developer. Emma salary is 5000$. Emma also knows ML and AI."
# escape dot
res = re.search(r"\.", str1)
print(res)
# Output ['.', '.', '.']
```

### square brackets ( [] )
- Used to Create your own patterns
- You cant get small letters with the `\w` or built in patterns.
*Syntax: [ pattern ]*

| **Metacharacter** | **Description** |
| ---- | ---- |
| `.` (DOT) | Matches any character except a newline. |
| `^` (Caret) | Matches pattern only at the start of the string. |
| `$` (Dollar) | Matches pattern at the end of the string |
| `*` (asterisk) | Matches 0 or more repetitions of the regex. |
| `+` (Plus) | Match 1 or more repetitions of the regex. |
| `?` (Question mark) | Match 0 or 1 repetition of the regex. |
| `[]` (Square brackets) | Used to indicate a set of characters. Matches any single character in brackets. For example, [abc] will match either a, or, b, or c character |
| `\|` (Pipe) | used to specify multiple patterns. For example, `P1\|P2`, where `P1` and `P2` are two different regexes. |
| `\` (backslash) | Use to escape special characters or signals a special sequence. For example, If you are searching for one of the special characters you can use a `\` to escape them |
| `[^...]` | Matches any single character not in brackets. |
| `(...)` | Matches whatever regular expression is inside the parentheses. For example, `(abc)` will match to substring `'abc'` |
## EXERSISE 1
1. Write a Regex That Filters the emails only from the following list
`john@gmail.com`
`natanhailu@yahoo.com`
`micky43@geeztecg.net`
`rexder@gmail.com`
`Hello there this is me`
`My phone number 0987654321`

```
import re
pattern="john@gmail.com\nnatanhailu@yahoo.com\nmicky43@geeztecg.net\nrexder@gmail.com\nHello there this is me\nMy phone number 0987654321"

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

matches = re.findall(pattern, emails)

print("Filtered emails:")
for match in matches:
    print(match)
```

```
output:
`john@gmail.com`
`natanhailu@yahoo.com`
`micky43@geeztecg.net`
`rexder@gmail.com`
```
2. Demlachewu is A software engineer and wanted to make a telegram bot that can delete links like https and ends with .com from the group, can u help him by writing the regex?
```
import re

# Define a pattern to match
pattern = r"(http|https)://[^\s]*\.com"

# Define a string to search
string = "Hello, here is a link to https://www.example.com and another link to http://example.com/foo"

# Search for the pattern in the string
matches = re.findall(pattern, string)

# Print the result
print(matches)

```

# Bash regex
- we can use awk, sed or grep to search for a particular pattern in bash.
- we are using grep for now.
- On bash terminal these metacharacters have meaning so, we have to escape them by adding `\` in front of the metacharacters
### EXERSISE
1. Write A bash code that can accept emails from user name and check if it is Valid email or not, using regex
```bash
#!/bin/bash

# Get email address from user
read -p "Enter your email address: " email

# Define regex pattern for email validation
regex="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Check if email is valid
if [[ $email =~ $regex ]]
then
echo "The email address '$email' is valid."
else
echo "The email address '$email' is invalid."
fi
```

#bash_loop
## Bash For loop
- there are two different techniques in using for loop in bash.
1. **C-style loop**: 
```sh
for ((initialize ; condition ; increment));
do
'COMMANDS' 
done
```
Example:
```sh
for ((i = 0 ; i < 10 ; i++))
do 
echo "Hello Friend" 
done
```

2.  **List/Range For Loops** :useful if you are working with a list of files (or strings), range of numbers, arrays, output of a command, etc.
```sh
for item in [LIST]
do
[COMMANDS]
done
```
For example:
```sh
for i in {1..10}
do
echo "Hello Friend"
done
```
```sh
for num in {10..0..-1}
do 
echo $num
done
output: 10,9,8,7,6,5,4,3,2,1,0
```

## Bash while loop
```sh
while [ condition ]
do
[COMMANDS]
done
```

**For example**, the following script uses a while loop that will print the first ten multiples of the number three:
```sh
#!/bin/bash

num=1
while [ $num -le 10 ]
do
echo $(($num * 3))
num=$(($num+1))
done

output: 3,6,9,12,15,18,21,24,27,30
```

## Bash Break statement
- The break statement terminates the execution of a loop and turn the program control to the next command or instruction following the loop.
**Example:**
```sh
#! /bin/bash

echo "count down for website launch"
i=10
while [ $i -ge 1 ]
do 
if [ i == 2 ]
then
echo "mission aborted"
fi
echo $i
((i--))
done
```

## Bash continue statement
- to skip a loop iteration. The loop continues and moves to the next iteration but the commands after the continue statements are skipped in that partcular iteration.
**Example:**
```sh
#!/bin/bash 
for ((i=0;i<=10;i++))
do 
if [ $(($i % 2)) -ne 1 ]
then 
continue 
fi 
echo $i 
done
```

## Bash until statement
- an until loop will keep running as long as test condition is false!
```sh
until [ condition ]
do 
[COMMANDS] 
done
```
**Example:**
```sh
#!/bin/bash 
num=1 
until [ $num -gt 10 ]
do 
echo $(($num * 3)) 
num=$(($num+1)) 
done
```

# Function in bash
- A Bash function is essentially a set of commands that can be called numerous times. The purpose of a function is to help you make your bash scripts more readable and to avoid writing the same code repeatedly.
```sh
#creating a function
function_name(){
body
}
#calling the function
function_name
```
**Example:**
```sh
#!/bin/bash

hello_world () {
   echo 'hello, world'
}

hello_world
```
## Variables Scope
- Global variables are variables that can be accessed from anywhere in the script regardless of the scope. In Bash, all variables by default are defined as global, even if declared inside the function.
- Local variables can be declared within the function body with the `local` keyword and can be used only inside that function. You can have local variables with the same name in different functions.
**Example:**
```sh
#!/bin/bash

var1='A'
var2='B'

my_function () {
  local var1='C'
  var2='D'
  echo "Inside function: var1: $var1, var2: $var2"
}

echo "Before executing function: var1: $var1, var2: $var2"

my_function

echo "After executing function: var1: $var1, var2: $var2"

```
```
output:
Before executing function: var1: A, var2: B
Inside function: var1: C, var2: D
After executing function: var1: A, var2: D

```