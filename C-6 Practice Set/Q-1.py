# Q. WAP to find the greatest of four no.s entered by the user.
# Method 1:

a = int(input("enter no. a: "))
b = int(input("enter no. b: "))
c = int(input("enter no. c: "))
d = int(input("enter no. d: "))

if a>b and a>c and a>d:
    print("a is greatest no.")
elif b>a and b>c and b>d:
    print("b is greatest no.")
elif c>a and c>b and c>d:
    print("c is greatest no.")
else:
    print("d is greatest no.")
