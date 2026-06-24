# Write a recursive function to calculate the sum of first n natural numbers.
def sum(a):
    if a <= 1:
        return 1
    else:
        return a + sum(a-1)
x = sum(7)
print(x)


def prod(b):
    return b + prod(b-1)
y = prod(5)
print(y)