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