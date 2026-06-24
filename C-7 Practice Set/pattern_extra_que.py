# EXTRA QUESTIONS OF CHATGPT:

# 1. Product of all even numbers from 1 to n:
"""n = int(input("Enter number: "))
product = 1
for i in range(1, n+1):
    if i % 2 == 0:
        product = product * i
print(f"Product of all even number from 1 to {n} is {product}")

# 2. Product of all odd numbers from 1 to x:
x = int(input("Enter  number: "))
product_odd = 1             # product naam ka variable already in use tha isliye product_odd liye
for i in range(1, x+1):
    if i % 2 != 0:
        product_odd = product_odd*i
print(f"Product of all odd number from 1 to {x} is {product_odd}")"""

''' 3. print inverted loop: 
*****
****
***
**
*
a = 5
for i in range(0,6):
    print("*"*(a-i))
'''

'''4. 


'''
a = 5
for i in range(1,6):
    print("*"*(i))

b = 5
for i in range(1,b+1):
    spaces = " "*(b-i)
    stars = "*"*(2*i-1)

    print(spaces + stars)

'''5. print
1
12
123
1234
12345 

d = 5
for i in range(1,d+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''

'''6. 
1
22
333
4444
55555

sol: 
Isko row-wise dekho:

Row 1 → 1 ek baar
Row 2 → 2 do baar
Row 3 → 3 teen baar
Row 4 → 4 chaar baar

Matlab:

Outer loop batayega kaunsi row hai (i)

Inner loop batayega kitni baar print karna hai (i times)

d = 6
for i in range(1,d+1):
    for j in range(i):
        print(i,end="")
    print()'''

'''7.
A
BB
CCC
DDDD
EEEEE 

sol: 
chr() ASCII value ko character mein convert karta hai.

chr(65)  # A
chr(66)  # B
chr(67)  # C

Aur:

64 + 1 = 65 -> A
64 + 2 = 66 -> B
64 + 3 = 67 -> C
which means:
ch = chr(65)
print(ch)
toh output = A   # agar 66 hota to output = B
a = 5
for i in range(1,a+1):
    print(chr(64+i)*i)'''