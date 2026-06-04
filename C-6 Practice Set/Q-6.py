"""
Q. write a program to calculate the grade of a student from his marks from given
scheme:
1. 90-100=> Ex
2. 80-90 => A
3. 70-80 => B
4. 60-70 => C
5. 50-60 => D
6. <50   => F
"""


# METHOD 1
maths = int(input("Enter Maths Marks: "))
phys = int(input("Enter Phys marks: "))
english = int(input("Enter english marks: "))
total = (maths+phys+english)/3

print(total)

if(total>90):
    print("Ex")
elif(total>80):
    print("A")
elif(total>70):
    print("B")
elif(total>60):
    print("C")
elif(total<50):
    print("F")


# METHOD 2
marks = int(input("enter marks: "))
if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<50):
    grade = "F"

print("your grade is:",grade)