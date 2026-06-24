# WAP to remove a given word from a list and strip it at the same time
# METHOD 1:

l = ["Devjeet","Ritu","Julli","Pama"]
def rem(l,word):
    for item in l:
        l.remove(word)
        return l
print(rem(l,"Julli"))

l2 = ["Devjeet","Ritu","Julli","Kitty"]
def rem_1(l2,alphabet):
    n = []
    for item in l2:
        if not(item == alphabet):
            n.append(item.strip(alphabet))
    return n 
print(rem_1(l ,"t")) 