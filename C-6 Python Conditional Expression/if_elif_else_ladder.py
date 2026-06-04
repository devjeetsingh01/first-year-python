# elif, multiple conditions

b = int(input("Enter you're age: "))
if(b>=20):
    print("Bingoooo")
    print("You are ready to go")
    print("Welcome to HOrror Heels")

elif(b<=0):    #if someone entered negative age so we have to tell user that's its wrong
    print("Warning put you're real age")

else:
    print("You are not eligible")

"""
LOGIC BEHIND: if,else,elif works jointly , first if condition of "if" is met than it prints whatever said in "if"
and elif and else becomes false.
if conditions of "if" is not met, then it go for "elif" if that too didn't true then it goes for another "elif" in 
program if that too didn't true that it goes for "else" and checks condition met or not
""" 

