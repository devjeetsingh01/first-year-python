s = {8, 7, 12, "Harry", [1,2]}
s[1,2] = 3
print(s)

"""
No, we cannot change the value inside a list in a set in python. in fact, we cannot even have a list
as an element in a set becuz sets in python requires all their elements to be immutable and hashable.
lists are mutable and are not hashable.
"""
