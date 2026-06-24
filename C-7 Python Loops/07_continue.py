


for i in range(5):
    print(i)
    if i == 2:
        continue  

"""continue is useless here because it's after print()

So flow is:

print happens first
then continue runs, but nothing to skip now

Key takeaway (important): 
continue only matters when it is before the code you want to skip"""

for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)

"""
Meaning:

👉 skip even numbers"""


for i in range(5):
    if i < 3:
        continue
    print(i)
"""Step:
0 → skip
1 → skip
2 → skip
3 → print
4 → print"""