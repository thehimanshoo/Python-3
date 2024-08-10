# Continue Statements

for n in range(2, 10):
    if n % 2 == 0:
        print(f"Even number :- {n}")
        continue
    print(f"Odd number :- {n}")
    
    
# Next example
print()

Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
offc_day = []
holiday = []

for day in Week:
    if day == "Sunday":
        holiday.append(day)
        continue
    offc_day.append(day)
    
print(f"{offc_day} :- Working Day")
print(f"{holiday} :- Today is Holiday")


# or In short way we can also code like this :-
for d in Week:
    if d == "Sunday":
       print(f"{d} => Hurrey!! Today is Holiday")
       continue
    print(f"{d} => Office day") 