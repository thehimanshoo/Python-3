# Comments in Python

# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
print(text)

# Operators in Python
# +, -, *, /, %
sum = 2+2
sub = sum - 2
mul = sum * 2
div = sum / 2   # classic division returns a float
div2 = sum // 2 # floor division discards the fractional part
rem = sum % 2   # The % operator returns the remainder of the division

print(f"Sum: {sum}")
print(f"Sub: {sub}")
print(f"Mul: {mul}")
print(f"Div: {div}")
print(f"Floor Division: {div2}")
print(f"Reminder: {rem}")

# In Python we use the ** operator to calculate powers
num1 = 5  # 5 squared
num2 = 5  # 5 to the power of 7
print(f"Square of 5 is: {num1**2}")
print(num2**7)

# The equal sign (=) is used to assign a value to a variable.

width = 20
height = 5
Area = width * height
print(f"Area of Rectangle: {Area}")

# operators with mixed type operands convert the integer operand to floating point
mixedOperand = 4 * 3.75 - 1
print(mixedOperand) #14.0

# To quote a quote, we need to “escape” it, by preceding it with \. Alternatively, we can use the other type of quotation marks
print('doesn\'t') # use \' to escape the single quote
print("doesn\'t") # or use double quotes instead
print('"Isn\'t," they said.')

''' In the Python shell, the string definition and output string can look different. The print() function produces a more readable output, 
 by omitting the enclosing quotes and by printing escaped and special characters '''

firstLine = 'First line.\nSecond line.'  # \n means newline
# without print(), special characters are included in the string
print(firstLine)  # with print(), special characters are interpreted, so \n produces new line

#This feature is particularly useful when you want to break long strings
print('Put several strings within parentheses '
        'to have them joined together.')


''' Strings can be indexed (subscripted), with the first character having index 0. 
There is no separate character type; a character is simply a string of size one '''
word = "Python"
print(word[0]) # character in position 0
print(word[5]) # character in position 5


''' Indices may also be negative numbers, to start counting from the right, 
Note that since -0 is the same as 0, negative indices start from -1. '''

print(word[-1]) # last character
print(word[-2]) # second-last character
print(word[-6]) # first character

# Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s.
print(word[:2] + word[2:])
print(word[:4] + word[4:])