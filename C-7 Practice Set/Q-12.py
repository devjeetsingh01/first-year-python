'''WAP to print:
***
* *
***
sol:
for i in range(3):
    if i == 1:
        print("* *")
    else:
        print("***")'''

'''extra quess.
*****
*   *
*   *
*   *
*****'''
# METHOD 1:
for i in range(5):
    if i == 1 or i == 2 or i == 3:
        print("*   *")
    else:
        print("*****")

# METHOD 2:
for i in range(5):
    if i == 0 or i == 4:
        print("*****")
    else:
        print("*   *")