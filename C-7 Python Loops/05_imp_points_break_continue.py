"""1. No break → else runs
2. break nahi mila → else run
3.Case A: print pehle, break baad mein
for i in range(5):
    print(i)
    if i == 2:
        break
here breakpoint will be included
Case B: break pehle, print baad mein
for i in range(5):
    if i == 2:
        break
    print(i)
here breakpoint will not be included

"""