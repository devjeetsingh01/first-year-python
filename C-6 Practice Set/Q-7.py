# Q. Write a program to find out whether a given post is talking about "Dev" or not.

# METHOD 1("WRONG WAY")
"""
a = input("enter name: ")
if(a == "Dev"):
    print("Found")
else:
    print("Not Found")
"""
# METHOD 2("RIGHT WAY")
""" 
A post can contain many words, so we check whether "Dev" is present anywhere in the text so 
that's why METHOD 1 is wrong.

a. contains basic method, in this in a post if we exactly put Dev then only it print "if"
condition otherwise it will print "else" condition. like post = Dev is very good boy. so this 
contain exact Dev so it'll print "if" condition.

b. contains PRO method, is case-insensitive this will detect dev, DEV, DeV.
"""
# BASIC METHOD:
post = input("enter post: ")
if("Dev" in post):
    print("This post is talking about Dev")
else:
    print("This post is not talking about Dev")

# PRO METHOD:
post_letter = input("enter post: ")
if("dev" in post_letter.lower()):
    print("This post is talking about Dev")
else:
    print("This post is not talking about Dev")


# Tip: Whenever a question asks "whether a word exists in a string" → think of the in operator.
#  It's one of the most useful string operations in Python.