# Write a recursive function to calculate the sum of first n natural numbers:

def natural_sum(a):
    if a == 1:
        return 1
    return a + natural_sum(a-1)
x = natural_sum(5)
print(x)

