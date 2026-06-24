# when a function calls itself repeatedly.
def show(n):
    if n == 0:   # this is base case ,means the value(here it is 0) where the value will stop
        return
    print(n,end=" ") 
    show(n-1)
show(5)
show(4)

print("END OF PROGRAM")


# Factorial(n) = n * factorial(n-1)
n = int(input("Enter Number: "))
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
factorial(n)
print(f"the factorial of {n} is {factorial(n)}")



