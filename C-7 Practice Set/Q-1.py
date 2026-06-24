# Q.1 WAP to print multiplication table of a given number using for loop
a = int(input("enter no: "))
for i in range(1,11):
    print(f"{a} x {i} = {a * i}")