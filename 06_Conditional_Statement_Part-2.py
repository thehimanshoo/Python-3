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

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print(f"Active user: {users}")

# Strategy:  Create a new collection
users_collection = {}
for user, status in users.items():
    if status == 'inactive':
        users_collection[user] = status
        print(f"New collection: {users_collection}")