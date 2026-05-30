s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s,len(s))

"""
INTERVIEW Q.
why this give 2 not 3?
ans: In python, comparison operators check values, if both values are same then data type(int,float,etc.)
doesn't matter to python

open terminal and see 30 == 30.0 press enter and output = True
"""