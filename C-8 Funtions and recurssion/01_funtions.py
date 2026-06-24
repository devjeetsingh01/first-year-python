'''A function is a group of statements performing a specific task.when a program gets bigger in 
size and its complexity grows,it gets difficult for a program tokeep track on which peice of code
is doing what!
A function can be reused by the programmer i a given program any number of'''

'''#IMP. FROM LINE 6 TO 12 IS "FUNCTIONAL DEFINITION"
def avg():   # here 'avg' is variable name
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    average = (a+b+c)/3
    print(average)
#IMP. FROM 13 TO 16 IS "FUNCTIONAL CALL"
avg()     # if we want output 3 times then write avg() for 3 times
avg()
avg()

print("END OF PROGRAM")
'''

'''TYPES OF FUNCTION:
1. Built in functions(Already present in python) eg. len(),print(),range() etc.
2. User defined functions(Defined by user)'''

# use of end="" function
'''print("dev",end=" $")
print("good")''' 

# ANOTHER WAY TO WRITE:
def cal_prod(a,b):
    print(a+b)
    return a+b
cal_prod(1,3)
cal_prod(2,4)
cal_prod(2,8)