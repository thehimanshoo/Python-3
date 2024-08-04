# Fibonacci series:
# the sum of two elements defines the next

num1, num2 = 0, 1
while num1 < 10:
    print(num1)
    num1, num2 = num2, num1+num2
    
# The keyword argument end can be used to avoid the newline after the output, or end the output with a different string
a, n = 0, 1
while a < 1000:
    print(a, end=",")
    a, n = n, a+n

# Since ** has higher precedence than -, -3**2 will be interpreted as -(3**2) and thus result in -9. To avoid this and get 9, you can use (-3)**2.
print("\n", -3**2)  # will get -9
print((-3)**2) # will get 9