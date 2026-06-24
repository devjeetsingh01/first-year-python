"""All the things which 'while loop' can do same thing but with higher efficiency a
for loop can also do.
When you know how many times something should repeat → use for loop.

When you don't know and repetition depends on a condition → use while loop."""

# for loop with lists
i = [1,7,8]
for item in i:
    print(item)
    
l = [1,2,5,7]
for i in l:
    print(i)

 # for loop with tuple 
t = (1,2,3,4)  # here t is talking about tuple
for i in t:
    print(i)    

# for loop with strings
s = "Devjeet" 
for i in s:
    print(i)
 

# RANGE FUNCION IN PYTHON:
"""The range() function in python is used to generate a sequence of number.
we can also specify the start,stop and step-size like 
range(start,stop and step-size)"""
# 1. range(stop)
for z in range(6):
    print(z)
# it will start from index 0 till 5, as last nno. is not included

# 2. range(start, stop) 
for x in range(1,7):
    print(x)
# 1 is included and 7 is not 

# 3. range(start, stop, step)
for k in range(10,2,-2):
    print(k)
for n in range(2,8,1):
    print(n)
