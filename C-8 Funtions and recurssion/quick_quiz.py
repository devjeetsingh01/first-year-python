#WAP  to greet a user with "GOOD DAY" using functions:

'''def name():
    a = input("Enter name: ")
    print("GOOD DAY")
name()
name()
name()
'''
# WAP to print the length of a list.(list is parameter)
'''cities = ["mumbai","delhi","jsr"]
name = ["dev",12,66]
def length(list):
    print(len(list),end=" ")    # there is no neccesary for adding end=" "

length(cities)
length(name) '''

# WAP to find to factorial of n.(n is parameter) using functions
# METHOD 1 Using for loop
n = int(input("enter number: "))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print(factorial)

# METHOD 2 using functions:
def calculate_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

calculate_factorial(4)

# WAP to convert USD to INR:
# METHOD 1:
def converter(usd_value):
    inr_value = usd_value*94.50
    print(f"{usd_value} USD = {inr_value} INR")

converter(73)

#WAP to print even or odd when a number is entered by user: 
a = int(input("Enter Number: "))
def num(a):
    if a%2 == 0:
        print("EVEN")
    elif a%2 != 0:
        print("ODD")
num(a)


def greet(name):
    print("Hello " + name)
greet("Devjeet")



def square(a):
    return a*a
result = square(5)
print(result)



# Default Arguement: 
'''def goodday(name,ending="Thank You"):
    print("Good Boy " + name)
    print(ending)
goodday("Devjeet")'''


def greet(name="Devjeet"):
    print("Hello " +name)
greet()
greet("Guest")

def num_1():
    for i in range(1,6):
        print(i,\n)
num_1(5)



