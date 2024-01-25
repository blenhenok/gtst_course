# Functions
- A function is a block of code that performs a specific task.
- Suppose, you need to create a program to create a blue circle. You can create two functions to solve this problem:
    - A function that create a circle function
    - A function that create a color function
- Dividing a complex problem into smaller chunks makes our program easy to understand and reuse.

- **Types of functions:**
    - *Standard library functions*: These are built-in functions in Python that are available to use. Almost all keywords are functions. For example: print(),len(),input()....
    - *User-defined functions* : We can create our own functions based on our requirements.

- creating function
```
def fun_name(parameter):
     function body
```
- calling function: we have to call the function so they are on the output.
```
fun_name(argument)
```

**Function argument**: is the actual value that is passed to the function when it is called.

**Function parameter** is a variable that is part of a function definition. It is a placeholder for the actual value that will be passed to the function when it is called. 
```
def add_numbers(x, y):
    return x + y
add_numbers(5,2)
#x,y are parameters
#5.2 are arguments
```

### Return statement
- A Python function may or may not return a value.
- If we want our function to return some value to a function call, we use the ‘return’ statement.
**Example:**
```
def add_numbers(x, y):
    return x + y
add_numbers(5,2)
output: nothing

def add_numbers(x, y):
    return x + y
print(add_numbers(5,2))
output : 7

```

## Recursion
- Recursion is process of defining something in terms of itself.
- In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.
**Example:**
```
def fun(x):
     if x == 1:
         return 1
     else:
         return(x * fun(x-1))
 print(fun(5))
 output => 120, because the factorial of 5 is 120
```

## Lambda
- A lambda function is a small anonymous function.
- A lambda function can take any number of arguments, but can only have one expression.
- The power of lambda is better shown when you use them as an anonymous function inside another function.
**Example:**
```
num = lambda a,b : a + b
print(num(2,4))
```

# Function takers
- Filter, map & reduce takes a function as an argument.

### Filter()
- The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not. and returns an iterator containing the elements of the iterable for which the function returns True.
- syntax:
`filter(function, iterable`
**Example:**
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
output => [2,4,6,8,10]
```
 
### Map() 
 - the map() function takes a function and an iterable as arguments and returns an iterator containing the results of applying the function to each element of the iterable.
 **Example:**
```
 numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
output => [1,4,9,16,25]
```

# Object-oriented programming (Oop)
- Python is an object oriented programming. This means mores things in python are objects.
- Objects are anything which can have action and name. Objects have attributes(properties) and methods(action or functions)
**Example** :  My Computer is an object because, it have.
    - Attribute: name, size, cpu, ram…
    - Behavior: Running games, playing music, displaying texts…

## python class
- Class is simply a place where we create our Object’s attribute and behavior. It is like a template
- a class is a blueprint for that object.
- Syntax:
```
class computer:
 #creating attribute
 name = ' '
 cpu = ' '
```
- After you create the Blueprint, now you can create the objects based on your class
- On the above example we created Class computer and gave it an attributes of name, cpu
- Conventionally Class Names Start with capital letter

## Creating object
- You can Create many Objects based on 1 class.      
- Syntax:
 ```
Var = classname()
 Var.attribute = “value”
```
**Example:**
```
a_cptr = computer()
a_cptr.name = 'hp laptop'
a_cptr.cpu = 'intel i5'

b_cptr = computer()
b_cptr.name = 'lenovo laptop'
b_cptr.cpu = 'intel i3'
```

## Giving Behaviors (Creating Methods)
- Functions are called methods on OOP
- Syntax on calling
`classname .method(object)`

```
class human:
    name=''
    age=''
    grade=''  

    def running(self):
        return 'i can run'
    def dancing(self):
        return 'i can dance'
    def eating(self):
        return 'i can eat'

human1 = human()
human1.name='blen'
human1.age=22
human1.grade='3rd year'  

print(f'my name is {human1.name}')
print(f'i am {human1.age}')
print(f'i am {human1.grade}')
print(f'my skills are {human.running(human1)},{human.dancing(human1)}, {human.eating(human1)}')

output => my name is blen
        i am a 3rd year
        i am 22
        my skills are i can run, i can dance, i can eat
```

## Python constructors
- a constructor is a special method that is called when an object is created. It is used to initialize the object’s attributes and perform any other setup that is required before the object can be used. The constructor method is named __init__ and is defined inside the class definition.
- Syntax of constructor declaration : 
```
class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

```
 - MyClass is the name of the class, and arg1 and arg2 are the arguments that the constructor takes. The self parameter refers to the instance of the object that is being created.
 - When an object of MyClass is created, the __init__ method is automatically called with the arguments that were passed to the constructor. The method then initializes the object’s attributes with the values of arg1 and arg2.
**Example:**
```
class Human:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def run(self):
        print("I can run!")

    def dance(self):
        print("I can dance!")

    def eat(self):
        print("I can eat!")

print(f'my name is {human1.name}')
print(f'i am {human1.age}')
print(f'i am {human1.grade}')
print(f'my skills are {human.running(human1)},{human.dancing(human1)}, {human.eating(human1)}')

output => my name is blen
        i am a 3rd year
        i am 22
        my skills are i can run, i can dance, i can eat
```

## Python inheritance
- inheritance is a way to create a new class that is a modified version of an existing class. The new class, called the child class, inherits all the attributes and methods of the existing class, called the parent class. The child class can then add new attributes and methods or override the existing ones.
Example:
```
class Child(Human):
    def __init__(self, name, age, grade, hobby):
        super().__init__(name, age, grade)
        self.hobby = hobby

    def play(self):
        print("I can play!")
child1 = Child("Your Name", Your Age, "Your Grade", "Your Hobby")

```

## Python encapsulation 
- encapsulation is a way to restrict access to methods and variables of a class from outside the class. It is achieved by making the methods and variables private, which means they can only be accessed within the class. This helps to prevent accidental modification of data and ensures that the object’s state is always valid.
- To implement encapsulation in Python, you can use the following conventions: Prefix the name of a method or variable with a double underscore __ to make it private.