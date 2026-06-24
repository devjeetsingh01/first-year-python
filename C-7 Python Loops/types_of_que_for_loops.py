s = "CAT"   # Question 1

for ch in s:
    print(ch)
    print("!")

for ch in "GO":    # QUESTION 2
    print("Hi")
    print(ch)

for i in range(3):   # QUESTON 3
    print("Hi")
    print(i)

for i in range(2):    # QUESTION 4
    print(i)

print("Done")

a = [1,2,3]      # QUESTION 5
for items in a:
    print(a)

for i in range(4):    # QUESTION 6
    print("printing...")
    if i == 2:
        continue
    print(i)


for i in range(3):    # QUESTION 7
    print("A")

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