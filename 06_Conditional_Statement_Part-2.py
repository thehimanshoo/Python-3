# for statements
words = ['Cat', 'Window', 'defenestrate']
for word in words:
    print(f"{word} :- {len(word)}")
    

# Create a sample collection
users = {
    'Alice': 'active',
    'Bob': 'inactive',
    'Charlie': 'active',
    'Diana': 'inactive'
}
print(f"Simple Collection:- {users}")

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print(f"Users having active status:- {users}")


# Strategy:  Create a new collection and push required value only
New_Collection = {}

# Checking for the required value to push in New_Collection
for newUser, newUserStatus in users.items():
    if newUserStatus == 'active':  # 'inactive' status people won't print because in above line of code, we've deleted 'inactive' status people
        New_Collection[newUser] = newUserStatus
        
print(f"New user collection object:- {New_Collection}")