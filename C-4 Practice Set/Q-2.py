students = []
a = int((input("Enter the marks of student 1: ")))
b = int((input("Enter the marks of student 2: ")))
c = int((input("Enter the marks of student 3: ")))
d = int((input("enter the marks of student 4: ")))
e = int((input("enter the marks of student 5: ")))

students.append(a)
students.append(b)
students.append(c)
students.append(d)
students.append(e)
students.sort(reverse = True)
# we can do in ascending or desending but i like desending 
print(students)

"""boom result does not show in ascending or desending order when 
we did not enter int(input() , this int function
because
 we are taking input in string format so we have to convert it into
   integer format
   """
