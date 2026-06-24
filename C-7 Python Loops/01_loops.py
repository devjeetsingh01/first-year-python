"""
sometimes we want to repeat a set of statements in our program. eg. print 1 to 
1000.
Loops make it easy for a programmer to tell the computer which set of instruction
to repeat and how.
"""

print(1)
print(2)
print(3)
print(4)
print(5)

# The same task can be done like this:
for i in range(1,6):
    print(i)
# Here 1 is inlcuded and 6 doesn't so output gives 1 to 5
