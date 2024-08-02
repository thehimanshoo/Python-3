# Lists in Python
List = [1, 2, 3, 4, 5, 6]
print(f"Lists:- {List}")

# Indexes of Lists
print(f"Items at Index 0:- {List[0]}")  # indexing returns the item
print(f"Items at Index 5:- {List[-1]}")  # returns last item of the List
print(f"Slicing returns a new List:- {List[3:]}")  # slicing returns a new list

# Lists also support operations like concatenation
newList = List + [10, 15, 20, 25, 30]
print(f"Concatenated List:- {newList}")

# Lists are a mutable type, i.e. it is possible to change their content
cubes = [1, 8, 27, 65, 125]  # something's wrong here,the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print(f"Updated List:- {cubes}")

# also add new items at the end of the list, by using the list.append() method
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(f"Append new value:- {cubes}")


''' Simple assignment in Python never copies data. When you assign a list to a variable, the variable refers to the existing list. 
    Any changes you make to the list through one variable will be seen through all other variables that refer to it. '''
    
rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgba) == id(rgb)
rgba.append("Alph")
print(f"Updated rgb List:- {rgb}")


''' All slice operations return a new list containing the requested elements. 
    This means that the following slice returns a shallow copy of the list '''
    
    
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(f"Correct rgba:- {correct_rgba}") # This will provide the shallow copy of the updated List
print(f"Existing rgba:- {rgba}")  # This will provide the original rgba List


# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"Letters list:- {letters}")

letters[2:5] = ['C', 'D', 'E']  # replace some values
print(f"Replaced value list:- {letters}")

# now remove some values
letters[2:5] = []  # clear the list by replacing the elements with an empty list
print(f"Removed value lists:- {letters}")


letters[:] = [] # clear the list by replacing all the elements with an empty list
print(f"Empty list replaced Lists:- {letters}")


# The built-in function len() to find the length of the list also applies to lists
print(f"Length of rgb list:- {len(rgb)}")   # will display 4


# It is possible to nest lists (create lists containing other lists), for example:
char = ['a', 'b', 'c']
num = [1, 2, 3]
nestList = [char, num]
print(f"Nest List:- {nestList}")
print(f"Accessing Nested List at index 0: {nestList[0][1]}")
print(f"Accessing Nested List at index 1: {nestList[1][2]}")