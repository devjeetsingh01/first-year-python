# Multiple "independent" checks → Multiple if , for eg.
"""
a = int(input("enter age: "))
b = int(input("enter salary: "))
if(a>22):
    print("YES")
else:
    print("NO")

if(b>20000):
    print("ABOVE AVERAGE")
else:
    print("BROKE")
"""
# Having multiple options of one decision:
balance = int(input("ENTER NO.: "))
if(balance<=2000):
    print("POOR BOII")
elif(balance==20000):
    print("RICH")
elif(balance>=80000):
    print("ULTRA RICH")
else:
    print("BROKE")