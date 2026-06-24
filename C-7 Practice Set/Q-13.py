'''WAP to print multiplication of n using for loops in reversed order

sol:'''
a = int(input("enter number: "))
for i in range(10,0,-1):
    print(f"{a} x {i} = {a*i}")