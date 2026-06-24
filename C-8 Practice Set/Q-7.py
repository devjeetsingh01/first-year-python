''' Write a python functon to print
***
**
* for n = 3'''

def pattern(n):
    for i in range(n):
        spaces = " " * (i)
        stars = "*" * (n-i)
        print(spaces + stars)
pattern(5)

