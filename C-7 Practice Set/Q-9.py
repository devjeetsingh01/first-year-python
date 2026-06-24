"""Q. WAP to print the following star pattern   # TYPE OF QUESTION(IMP.) 
  *
 ***
*****    for n = 3  """
"""
sol:
to solve these types of question , follow these steps:
Step 1: Stars count karo

row 1 = 1 start
row 2 = 3 start
row 3 = 5 start
har bar 2 ka increase ho rha ha
pattern observed = 2*i-1 
i=1 -> 2(1)-1 = 1
i=2 -> 2(2)-1 = 3
i=3 -> 2(3)-1 = 5
 
step 2: spaces count karo (stars ko middle ek proper format mei lane ke liye spaces)
  *     # 2 space required
 ***    # 1 space required
*****   # 0 space required   here it's 3 rows so n = 3
pattern observed: spaces = n-1
check:
3-1 = 2
3-2 = 1
3-3 = 0

Step 3: Har row print karo

Row 1:
spaces = " " * 2
stars = "*" * 1
Row 2:
spaces = " " *1
stars = "*" * 3
Row 3:
spaces = " " * 0
stars = "*" * 5

step 4: loops lagao
for i in range(1,n+1):
    spaces = " " * n-1
    stars = "*" * (2*1-1)


n = 3
for i in range(1,n+1):
    spaces = " " * (n-i)
    stars = "*" * (2*i-1)

    print(spaces + stars)
 """
# THE REAL ONE:

n = int(input("enter the number: "))              
for i in range(1,n+1):
    print(" "*(n-i), end="")   # 
    print("*"*(2*i-1), end="")
    print("\n")

  
a = int(input("enter number: "))    # for a = 5
for i in range(1,a+1):
    print(" "*(a-i), end="")
    print("*"*(2*i-1), end="")
    print("")    #  we can also do print("\n")

# WHY WE ADD end="", ye new line form hone nhi dega like:
print("Hello word",end="")
print("Devjeet")
# another example
for i in range(1,4):
    print(i,end="")
