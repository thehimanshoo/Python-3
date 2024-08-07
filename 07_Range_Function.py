# If you need to count through a list of numbers, you can use the `range()` function. It helps you create a list of numbers in order.
for i in range(5):
    print(f"{i} =>  Hello World")
    

''' The ending number is not included in the list made by `range()`. For example, `range(10)` makes a list of 10 numbers, 
    from 0 to 9, which matches the positions (or indices) in a list of 10 items. You can also start the range at a different 
    number or change how much it goes up or down each step (this is called the 'step' and can even be negative) '''
    
print()  # Printing one empty line to seperate above line

for i in range(5, 10):  # To loop through the positions in a list
    print(f"{i} :- Hello World")
    
    
#  To-Loop through the positions in a list with some fixed difference
print()  # Printing one empty line to seperate above line

for j in range(-10, -100, -30):  # Loop through numbers starting from -10, decreasing by 30 each time, until reaching -100 (not included)
    print(f"Decreasing by 30 each time until reaching -100 (not included) => {j}")
    
   
    
''' To loop through the positions in a list, we can use `range()` and `len()` '''
print()

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for i in range(len(months)):
    print(f"{i} :- {months[i]}")
    
    
''' We call an object "iterable" if we can use it to get items one after another until there are no more items left. 
    The `for` loop is one way to use an iterable, and the `sum()` function is another example that works with iterables. '''
    
print()

# To find Fibonacci series we can also find directly like this :-
print(sum(range(5)))  # 0 + 1 + 2 + 3 + 4