# METHOD 1
maths = int(input("Enter Marks: "))
english = int(input("Enter marks: "))
phys = int(input("Enter marks: "))

if(maths>33):
    print("Pass")
else:
    print("FAIL")
if(english>33):
    print("Pass")
else:
    print("Fail")
if(phys>33):
    print("Pass")
else:
    print("Fail")


total_percentage = (maths+english+phys)*100/300
print(total_percentage)

# METHOD 2
maths = int(input("Enter MATHS Marks: "))
english = int(input("Enter ENGLISH marks: "))
phys = int(input("Enter PHYSICS marks: "))

total_percentage = (maths+english+phys)*100/300

if(maths>=33 and english>=33 and phys>=33 and total_percentage>40):
    print("YOU HAVE PASSED" , total_percentage)
else:
    print("YOU HAVE FAILED TRY NXT YR")