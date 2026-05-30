# 1. len()
a = {1,2,3}
print(len(a))

# 2. .remove()
b = {1,2,3,4}
b.remove(1)
print(b)

# 3. .clear(), empties the set 
c = {1,4,5,6}
c.clear()
print(c)

# 4.  .pop(), removes random number from set
d = {1,3,5,7}
d.pop()
print(d)

# 5. .union   
s1 = {1,2,3}
s2 = {4,5,6}
print(s1.union(s2))

# 6. .intersection()
s3 = {1,3,5,8,9}
s4 = {1,8,0,12}
print(s3.intersection(s4))

# 7. . difference()
s5 = {2,3,6}
s6 = {2,7,8}
print(s5-s6)
# or we can do print(s5.difference(s6))

# 8. .symetric difference : elements not present in both sets
s7 = {1,5,9,10}
s8 = {1,5,8}
print(s7^s8)

# 9. .issubset() and issuperset() :output will be T/F  
s8 = {1,5,8}
s9 = {1,5,8,9}
print(s8.issubset(s9))

print(s8.issuperset(s9))
print(s9.issuperset(s8))

# 10. .discard()
s8 = {1,5,8}
s8.discard(1)
s8.discard(9)
print(s8)

# INTERVIEW QUESTION.
"""
What's the difference b/w discard,remove,clear,pop ?
ans: 1. discard is same as remove but if some element is not present in 
set and we print discard output = none and in remove , output = error
2. clear, cleans all elements in set 
3. pop, removes random element from set(becz sets are unordered so that's
why pop removes random element) 
"""
 
 