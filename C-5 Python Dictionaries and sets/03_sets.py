# to print empty "dictionary" a = {} then print(a)
# INTERVIEW QUESTION:
"""
empty set kaise banaye ?
ans: shown below 
precaution: DON'T USE x = set() as it will create an empty dict.
"""
a = {1,2,3}
b = set()


# 2. elements don't repeat in sets
c = {1,2,3,3,3,3,}
print(c)

# PROPERTIES OF SETS
"""
1.Sets are unordered: means element's order doesn't matter
2.are Unindexed : Cannot access elements by index ,"numbering will doesn't 
start with 0."
3.there is no way to change items in sets
4.they cannot contain duplicate values means repititive value print nhi
hoga eg. a = {1,1,1,2} then print(a) then output gives {1,2}
"""