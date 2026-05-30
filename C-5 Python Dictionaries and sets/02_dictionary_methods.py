# 1. .items() returns a list of(keys,values)tuples

marks = {
    "Devjeet": 100,
    "Rohan": 33,
    "Shubham":44
    }
print(marks.items())

"""
 2. .keys() returns a list containing dictionoary's key means 
 left side wala value like Devjeet , rohan , shubham ye sb left
 mei ha, ab chahe left side naam ho ya number ye left side wala hi
 print karega
 """
print(marks.keys()) 

"""
3. .values() right wala value like 100,33,44 toh ye sb right mei ha
ab chahe right side naam ho ya number ye right side wala hi print
karega
"""
print(marks.values())

"""
4. .update() , updates dictionary with supplied key value pair
ham log existing keys ka value change kar skte hain like a.(shown
below) and value ka keys bhi change kr skte same as a. Also ham 
log new both keys and values bhi add kar skte hain apne existing 
dictionary mei like b.(shown below)
"""
# a.
marks.update({"Rohan": 66})
print(marks)
# b.
marks.update({"Ram": 98})
print(marks)
 
# in more proffesional way we can do  it 
marks.update({"Rohan": 67 ,"Ram": 98})
print(marks)


# 5. .get() 
print(marks.get("Devjeet"))

# INTERVIEW QUESTION:
"""
so now question is .get("Devjeet") or marks["Devjeet"] dono same
result dega toh .get() kyu use kare ? 
Ans: marks["Devjeet2"] likh de toh ye error dega but 
.get("Devjeet2") karenge toh none dega
LET'S TRY IT OUT
"""
# print(marks.get("Devjeet2"))
# print(marks["Devjeet2"])

# 6 .pop() ,
student = {
    "name": "Dev",
    "age": 29,
    "class": "CSE"
}
x = student.pop("age")
print(x)
print(student)

# 7 .popitem() , removes the last inserted item 
y = student.popitem()
print(y)
print(student)
