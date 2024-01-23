## Programming languages
- programming language, any of various languages for expressing a set of detailed instructions for a digital computer.
- It is language which helps to communicate with computers (they are not able to understand human languages)
## Algorithm
- An algorithm is a set of instructions that a computer must perform to solve a well-defined problem. It essentially defines what the computer needs to do and how to do it. Algorithms can instruct a computer how to perform a calculation, process data, or make a decision.
## Program
- A program is a concrete implementation of an algorithm. While algorithms are abstract, programs are tangible and can run on a computer. After developing an algorithm, programmers can build the program by translating the algorithm into code.

## Evolution of I/O
- Early in the history of computing, programs were submitted on punch cards with all the data they required and executed together with other programs that used the same libraries. Output was to a line printer.
- Later developments introduced interactive processing which allowed the user to provide data while the program was running. This normally takes place in a Question & Answer format.
## Generation of computers
- *First Generation*: Vacuum Tubes  =>  punch cards
- *Second Generation*: Transistors   => Programming started here with Assembly
- *Third Generation*: Integrated Circuits => BASIC, COBOL, Pascal, Fortran, C, C++, Perl etc.
- *Fourth Generation*: Microprocessors => Python, SQL, MATLAB
- *Fifth Generation*: Artificial Intelligence

# Types of programming languages
- Computers Understand binary(0/1) , humans don’t understand this
- The more they become low to the machine they are faster; The more they become like human language they are slower.
- So based on the closeness of the language to humans we classify it into 3:
1. ***Low-level programming languages***: - are machine-oriented and provide little or no abstraction from the hardware. They are used to write system software and device drivers that require direct access to the hardware. Examples of low-level languages include assembly language and machine language.
2. ***Middle-level programming languages*** are a combination of low-level and high-level languages. They provide some level of abstraction from the hardware while still allowing direct access to the system resources. Examples of middle-level languages include C and C++.
3. ***High-level programming languages*** are designed to be easy to read and write. They provide a high level of abstraction from the hardware and are used to write application software. Examples of high-level languages include Python, Java, and Ruby.

## How high-level programming languages work?
1. ***compiled language*** is a programming language in which we use a compiler to compile and execute our code. the compilers are generally translators that generate machine level code from our written source code.   
    **Example:** C, C++, C#, Cobol, Fortran, Java, Visual Basic, Smalltalk
2. ***interpreted language*** is a programming language in which without compiling a program into machine-language instructions we can execute instructions directly and freely. The interpreter executes the program line by line. Interpreted a language gives many additional flexibility over compiled implementations like, platform independence, dynamic scoping, dynamic typing etc.   
    **Example:** Python, Ruby, Perl, Pascal, Lisp, BASIC, APL
## History of python
- Python was developed by Guido van Rossum in the late eighties and early nineties at the National Research Institute for Mathematics and Computer Science in the Netherlands.
- Python is derived from many other languages, including ABC, Modula-3, C, C++, Algol-68, Smalltalk, and Unix shell and other scripting languages.
- Python is now maintained by a core development team at the institute, although Guido van Rossum still holds a vital role in directing it's progress

## IDE ( Integrated Development Environment )
- Is a Software that helps to write & run a Specific Programming language. 
    **Example**: PythonIDE

## Code Editors
- are software those can help to write any kind of programming languages. And also by adding some compiling/ interpreting feature they can run programs/scripts 
    **Example**: Sublime, Vscode

# Python programming

### comments
 `#`: for one liner comment
```
''' 
for multi line comments, it can also be used in string. 
'''
```

### output (displaying)
- we use `print()` to display text on the screen
    - **sep= ' '**: is used to print multiple items separated by special character, we use the sep parameter.
    - **end= ' '**: to remove white space or to display different items on the same line.
    *Example*: print('hello' , 2023 , 'students', sep'?')
        output -> hello ? 2023 ? students

## Variables
- Variables are a value holders (containers), They store data.
- We give some value to some word.
**Example** : a = 10 => from now on my python program knows the value of a is 10.
- The process of giving value to word is called Variable Declaration
- The word that holds the data is called Identifier  
- We can Print value of variables by giving the identifier
- We can change value of variable in a code.
```
a = 10
print('we have', a, 'oranges in the storage') 
output => we have 10 oranges in the storage

a = 9000
print('we have', a, 'oranges in the storage') 
output => we have 9000 oranges in the storage
```

## formatting string
- format specifier here to tell Python where to substitute the value of  a variable which represents a specified value.
**Example:**
```
a = 'we have gtst class'
print(f'at 2 o'clock {a}')
output => at 2 o'clock we have gtst class

or 
a = 'i have gtst class'
b = 'my name is blen'
print(f(b,a)'{}, ',student of gtst', {}, 'at 2')
output => my name is blen ,student of gtst i have gtst class at 2.
```

- it can also be used as:
```
a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')
output => Five plus ten is 15 and not 30.
```

## Data types in python
- You can Identify The type of a variable with the keyword ‘**type()**’

| types |  | description |
| ---- | ---- | ---- |
| Text Type: | `str` | holds sequence of characters |
| Numeric Types: | `int`, `float`, `complex` | holds numeric values |
| Sequence Types: | `list`, `tuple`, `range` | holds collection of items |
| Mapping Type: | `dict` | holds data in key-value pair |
| Set Types: | `set`, `frozenset` | holds collection of unique items |
| Boolean Type: | `bool` | holds either true or false |
| Binary Types: | `bytes`, `bytearray`, `memoryview` | represents sequence of bytes or the memory of an object |
| None Type: | `NoneType` | represents the absence of a type |
### Numeric type
- **int(integer)** - holds signed integers of non-limited length.
- **float** - holds floating decimal points and it's accurate up to 15 decimal places.
- **complex** - holds complex numbers.
### String data
- String is a sequence of characters represented by either single or double quotes.
### Sequence type
1. **Lists**: is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ]. 
    *Example*:  languages = ["Swift", "Java", "Python"]
    - To access items from a list, we use the index number (0, 1, 2 ...). For example, languages[0] will give as swift.
    - we can add or modify objects to the list by using the key `.append`
    *Example*: language.append= 'amharic'
        output => swift, java, pyhton, amharic

2. **Tuple**: is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.
    - we use the parentheses () to store items of a tuple. 
    *Example*: product = ('Xbox', 499.99)
    - Similar to lists, we use the index number to access tuple items in Python
### Dictionary types
- Python dictionary is an unordered collection of items. It stores elements in key/value pairs.
**Example**: user1 = {'username':’nathan26,’password’:’word'}
- username and password = key
- nathan26 & word = value
- We use keys to retrieve the respective value. But not the other way around. For example,
