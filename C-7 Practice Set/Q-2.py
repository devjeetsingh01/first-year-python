"""Q.2 WAP to greet all the person names stored in a list and which starts with S
list = ["Harry" ,"Soham", "Sachin, "Rohan"]
sol:"""
# METHOD 1:
list = ["Harry" ,"Soham", "Sachin", "Rohan"]
for name in list:
    if name.startswith("S"):
        print("Hello" , name)

# METHOD 2:
list1 = ["Harry" ,"Soham", "Sachin", "Rohan"]
for name in list1:
    if name.startswith("S"):
        print(f"Hello {name}")

# my curiosity:
list3 = ["Devjeet" , "Ritu", "Rajinder", "julli", "Roti"]
for name in list3:
    if name.startswith("R"):
        print(f"Hello {name}")