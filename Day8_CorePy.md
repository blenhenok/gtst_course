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
1. ***Arithmetic operations***: are used to perform basic mathematical operations.

|Operator|Description|Syntax|
|---|---|---|
|+|Addition: adds two operands|x + y|
|–|Subtraction: subtracts two operands|x – y|
|*|Multiplication: multiplies two operands|x * y|
|/|Division (float): divides the first operand by the second|x / y|
|//|Division (floor): divides the first operand by the second|x // y|
|%|Modulus: returns the remainder when the first operand is divided by the second|x % y|
|**|Power: Returns first raised to power second|x ** y|
2. ***Comparison operators***: it compares the values. It either returns True or False according to the condition.

|Operator|Description|Syntax|
|---|---|---|
|>|Greater than: True if the left operand is greater than the right|x > y|
|<|Less than: True if the left operand is less than the right|x < y|
|==|Equal to: True if both operands are equal, comparison operator |x == y|
|!=|Not equal to – True if operands are not equal|x != y|
|>=|Greater than or equal to True if the left operand is greater than or equal to the right|x >= y|
|<=|Less than or equal to True if the left operand is less than or equal to the right|x <= y|
3. ***Assignment operators***: are used to assign values to the variables.

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
4. ***Logical operators***: perform Logical AND, Logical OR, and Logical NOT operations. It is used to combine conditional statements.

|Operator|Description|Syntax|
|---|---|---|
|and|Logical AND: True if both the operands are true|x and y|
|or|Logical OR: True if either of the operands is true|x or y|
|not|Logical NOT: True if the operand is false|not x|
5. ***Bitwise Operators***: Computers Work with Binaries, On our computer everything have a binary value.  ( also called bit)
- On python there is a keyword called bin(Decimal) this helps to Show you the binary value of Decimal
    - True have a value of 1
    - False have a value of 0
- Bitwise Operators Used to do math(Logical operations) on The binary value of The expression.
- act on bits and perform bit-by-bit operations.

