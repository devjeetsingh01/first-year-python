"""for i in range(3):
    for j in range(2):
        print(i, j)
Trick 1: Expand it manually

Pretend Python writes this:

i = 0
j = 0 → print(0, 0)
j = 1 → print(0, 1)

i = 1
j = 0 → print(1, 0)
j = 1 → print(1, 1)

i = 2
j = 0 → print(2, 0)
j = 1 → print(2, 1)
Output:

0 0
0 1
1 0
1 1
2 0
2 1

Output:

0 0
0 1
1 0
1 1
2 0
2 1"""

# IMPORTANT TIP:
"""The trick

Whenever you see:

for i in range(...):
    statement1
    for j in range(...):
        statement2
    statement3

Think:

i = first value
    statement1
    inner loop completely
    statement3

i = second value
    statement1
    inner loop completely
    statement3

IN SIMPLE WORDS: "For each value of i, run EVERYTHING inside me."
First iteration (i = 0)

Python enters the loop and runs everything inside:

A
0
1
B   
    
Second iteration (i = 1)

Again it runs everything inside:

A
0
1
B
    
 """


for i in range(3):       # QUESTION 8
    for j in range(2):
        print("Hi")  

""" Final output
Hi
Hi
Hi
Hi
Hi
Hi"""
 