''' 
                                            Break Statements
                                           ------------------
                                           
    - The `break` statement stops the nearest `for` or `while` loop.
    - A `for` or `while` loop can have an `else` part.
    - In a `for` loop, the `else` part runs after the loop finishes all its steps.
    - In a `while` loop, the `else` part runs after the loop's condition is no longer true.
    - The `else` part does not run if the loop was stopped by `break`. 
'''

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number")
        
        
# To find an Even or Odd number
print();

even_number = {}
odd_number = {}

for num in range(2, 11):
    if num % 2 == 0:
        even_number[num] = True
    else:
        odd_number[num] = True
            
print(f"Even number :- {list(even_number.keys())}")        
print(f"Odd number :- {list(odd_number.keys())}")        