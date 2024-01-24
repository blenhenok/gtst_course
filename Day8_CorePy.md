## Indexing
- The list index always starts with 0. Hence, the first element of a list is present at index 0, not 1.
- in listing we seen the indexing.
- we have also have negative indexing
    **Example**: a= ['abebe', 'belete', 'chala']
                -3,      -2,          -1
     print(a[-1])  , output => chala
 - indexing also works for strings and tuples
    **Example**:  b = 'software'
     print(b[2])  , output => f
     print(b[-3]), output => a
## Slicing
- *Syntax*:
`Mylist[ start : stop : step ]`
- Slicing is indexing syntax that extracts a portion from a list. If a is a list, then a[m:n] returns the portion of a:
    - Starting with position m
    - Up to but not including n
    - Negative indexing can also be used
- Python uses default step as 1, sometimes no need to tell/put it
- Also default stopping index is the final, still no need to tell for this kind of purpose
     **Example**: a= ['abebe', 'belete', 'chala', 'delta']
         print(a[-1:0:-2]), output => belete

# User input handling
## By input functions
- *Syntax*:    `var = input(“Text you like to display: ”)`
- it Will accept the input and stores on variable
- You can change the input type to int() float() eval() str().
    **Example:** a = input("enter your age ") , let input = 30
        print(a) , output=> '30'

    a = int(input("enter your age "))
        print(a), output => 30
- because every input is received as a string.

## Argument
- This help us to get the input from the command lines
- ***Shell***:   python gtst.py arg1 arg2 arg3
- and it goes like
```
import sys
name = sys.argv[1]
info = sys.argv[2]
print(f"my name is {name} "i am a " {info})
```

```sh
python a.py blen student
> my name is blen i am a student
```

# Operators
- Operators are special symbols that perform operations on variables and values.
## Arithmetic operations: 
- it is used to perform basic mathematical operations.

|Operator|Description|Syntax|
|---|---|---|
|+|Addition: adds two operands|x + y|
|–|Subtraction: subtracts two operands|x – y|
|*|Multiplication: multiplies two operands|x * y|
|/|Division (float): divides the first operand by the second|x / y|
|//|Division (floor): divides the first operand by the second|x // y|
|%|Modulus: returns the remainder when the first operand is divided by the second|x % y|
|**|Power: Returns first raised to power second|x ** y|
## Comparison operators
- it compares the values. It either returns True or False according to the condition.

|Operator|Description|Syntax|
|---|---|---|
|>|Greater than: True if the left operand is greater than the right|x > y|
|<|Less than: True if the left operand is less than the right|x < y|
|==|Equal to: True if both operands are equal, comparison operator |x == y|
|!=|Not equal to – True if operands are not equal|x != y|
|>=|Greater than or equal to True if the left operand is greater than or equal to the right|x >= y|
|<=|Less than or equal to True if the left operand is less than or equal to the right|x <= y|
## Assignment operators
- it is used to assign values to the variables.

| Operator | Description | Syntax |
| ---- | ---- | ---- |
| = | Assign the value of the right side of the expression to the left side operand | x = y + z |
| += | Add AND: Add right-side operand with left-side operand and then assign to left operand | a+=b     a=a+b |
| -= | Subtract AND: Subtract right operand from left operand and then assign to left operand | a-=b     a=a-b |
| *= | Multiply AND: Multiply right operand with left operand and then assign to left operand | a=b     a=a b |
| /= | Divide AND: Divide left operand with right operand and then assign to left operand | a/=b     a=a/b |
| %= | Modulus AND: Takes modulus using left and right operands and assign the result to left operand | a%=b     a=a%b |
| //= | Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand | a//=b     a=a//b |
| **= | Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand | a=b     a=a b |
## Logical operators
- it perform Logical AND, Logical OR, and Logical NOT operations. It is used to combine conditional statements.

|Operator|Description|Syntax|
|---|---|---|
|and|Logical AND: True if both the operands are true|x and y|
|or|Logical OR: True if either of the operands is true|x or y|
|not|Logical NOT: True if the operand is false|not x|
## Bitwise Operators
- Computers Work with Binaries, On our computer everything have a binary value.  ( also called bit)
- On python there is a keyword called bin(Decimal) this helps to Show you the binary value of Decimal
    - True have a value of 1
    - False have a value of 0
- Bitwise Operators Used to do math(Logical operations) on The binary value of The expression.
- act on bits and perform bit-by-bit operations.

|OPERATOR|NAME|DESCRIPTION|SYNTAX|
|---|---|---|---|
|&|Bitwise AND|Result bit 1,if both operand bits are 1;otherwise results bit 0.|x & y|
|\||Bitwise OR|Result bit 1,if any of the operand bit is 1; otherwise results bit 0.|x \| y|
|~|Bitwise NOT|inverts individual bits|~x|
|^|Bitwise XOR|Results bit 1,if any of the operand bit is 1 but not both, otherwise  results bit 0. |x ^ y|
|>>|Bitwise right shift|The left operand’s value is moved toward right by the number of bits specified by the right operand. shifts the stated amount of bits to the right. |x>>|
|<<|Bitwise left shift|The left operand’s value is moved toward left by the number of bits specified by the right operand. shifts the stated amount of bits to the left. |x<<|
- The integers are first converted into binary and then operations are performed on each bit or corresponding pair of bits, hence the name bitwise operators. The result is then returned in decimal format.
**EXAMPLE:**
```
a = 10
b = 4
print(a & b) 
print(a | b) 
print(~a) 
print(a ^ b) 
print(a >> 2) 
print(a << 2) 
```
- the outputs will be:
```
a = 10 = 1010
b = 4 = 0101
a & b = 1010 & 0101 = 0000 = 0 

a | b = 1010 | 0101 = 1110 = 14 (decimal form)

a = 10 = 1010(binary)
~a = 1010 =>  1010 +1 => 1011 (1st complement) = -11(decimal)

a ^ b = 1010 ^ 0101 = 1110 = 14

a<<2 = 1010.00 => 101000 = 40(decimal)

b>>1 = 010.1 => 1(decimal)

```

# If else conditions
- used to run a block of code when a certain conditions are met. if not it ignores the statement and moves on to the next one.

```
if condition1:
     statement
elif condition2:
     statement
 else:
     statement
     
```

# Logical Errors ( Exceptions)
- Errors that occur at runtime (after passing the syntax test) are called exceptions or logical errors.
- For instance, they occur when we
    - try to call an index that is greater than the list have causes ( Index Error )
    - try to divide a number by zero (Zero Division Error)
    - When you have error on your syntax (Name Error) and so on.
- So specially when errors occur on runtime this causes a huge damage on our program so we have to handle it.
## Error handling
- For handling errors we use try…except blocks.
```
try: 
     code that may cause exception
except:
     code to run when exception occurs
```
**Example:** 
```
try:
     a = [2,4,6,8]
     print(a[5])
except zerodivisionerror:
     print("denominator can't be 0")
except indexerror:
     print("index out of bound")
```

# LOOP
- they are used to run a block of code repletely for a certain period of times.

## For loop
- It is used to iterate over any sequences such as list, tuple, string, etc.
- syntax:
```
if val in sequence:
     statement(s)
#val is a variable that hold the iteration from the sequence
#sequence is the list, tuple or range we are working on
```
***Example:***
```
a = ['china', 'asia', 'africa']
for i in a:
     print(i)
```

#### Range keyword
- A range is series of values between two numeric intervals.    
- syntax: `range(size)`
**Example:**
```
a = range(4)
for i in a:
     print(i)
 output => 0  1  2  3
```

#### Len keyword
- A len is used to show the length of a sequence may be list, tuple or staffing.    
- syntax: `len(list)`
**Example:**
```
a = ['china', 'asia', 'africa']
print(len(a))
output => 3

for i in range(len(a)):
     print(i)
 output => 0 1 2 3 4 5
```

## While loop
- Python while loop is used to run a specific code until a certain condition is met.
- syntax:
```
initialization
while condition:
     statement
 or 
 
while true:
    statement
```
***Example***:
```
i=1
n=5
while i <= n:
     print(i)
     i=i+1
output => 1 2 3 4 5
```

- **the difference between for and while loops**:
    - The for loop is usually used when the number of iterations is known.
    - while loop is usually used when the number of iterations are unknown. 
    - For loops: ends when the iteration is finished.
    - While loops: end when the condition is false.

***Break***: used to exit from infinite loop.
