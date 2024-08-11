'''
                                                                            Pass Statements
                                                                           -----------------
    
    The pass statement does nothing. It's used when you need a statement in your code but don't want it to do anything.                                                                     
'''

# 1. Empty Function
# We might use pass to define a function that you haven't implemented yet.

def my_function():
    pass  # No code here yet, but it's a valid function


# 2. Placeholder for Future Code
# We can use pass as a placeholder in code where you plan to add functionality later.

def some_function():
    pass  # To be implemented later

class MyClass:
    def method(self):
        pass  # To be implemented later


# 3. Empty Class
# We can define an empty class with pass when you are planning to add methods or properties later.

class MyEmptyClass:
    pass  # Empty class, no methods or properties yet


# 4. Conditional Statements
# We can use pass in conditional statements when you have not decided what code to write yet.

x = 10

if x > 0:
    pass  # Do nothing if x is positive
else:
    print(f"{x} is not positive")