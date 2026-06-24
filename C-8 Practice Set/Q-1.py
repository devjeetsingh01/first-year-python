# WAP using functions to find the greatest of three numbers
def largest(a,b,c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    elif c > b and c > a:
        return c
x = largest(10,20,30)
print(x)