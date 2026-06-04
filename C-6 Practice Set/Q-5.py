# very imp Q.
# Q.WAP which finds out whether a given name is present in a list or not.

# METHOD 1
a = ["gogo", "momo", "jojo", "koko"]
print("ero" in a)

"""
IN LIST IF WE WANT TO CHECK SOMETHING, THEN WE USE:
1. "in" and "not in" operators:
like in a ,there is no element named "ero" so output = false
2.IF and ELSE:
given below:
3. .count(): if a desired word is present in that list it will give 1 or 2 ,but
atleast 1, if not then give 0
"""
# METHOD 2
if "ero" in a:
    print("FOUND")
else:
    print("NOT FOUND")