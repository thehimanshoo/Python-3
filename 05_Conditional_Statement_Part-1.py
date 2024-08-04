'''
                                                                    Types of Conditional Statements in Python
                                                                   -------------------------------------------

1. `if` Statement:
   - Executes a block of code if a specific condition is true.

2. `if-else` Statement:
   - Executes one block of code if a condition is true, and another block if the condition is false.

3. `if-elif-else` Statement:
   - Checks multiple conditions in sequence. Executes different blocks of code depending on which condition is true. The `elif` part stands for "else if" and is optional, as is the `else` part.

4. Nested `if` Statements:
   - An `if` statement inside another `if` statement, allowing for more complex condition checking.

5. Conditional Expressions (Ternary Operator):
   - A shorthand way to write an `if-else` statement in a single line, assigning a value based on a condition.
   
'''

# if Statements
x = 10
if x > 5:
    print("if statement Example output:- x is greater than 5")
    
    
# if-else Statement
x = 5
if x > 5:
    print("x is greater than 5")
else:
    print("if-else Example output:- x is not greater than 5")


# if-elif-else Statement    
num = int(input("Enter an integer: "))
if num < 0:
    print("Enter non-negative number")
elif num == 0:
    print("Zero")
elif num == 1:
    print("One")
elif num == 2:
    print("Two")
else:
    print("if-elif-else Example output:- More than 2")
    
 
# Nested if Statement
x = 10
if x > 5:
    if x < 15:
        print("Nested-if Example output:- x is between 5 and 15")
    
    
# Conditional Expression (Ternary Operator)
x = 10
result = "x is greater than 5" if x > 5 else "x is not greater than 5"
print(f"Ternary Operator Example output:- {result}")