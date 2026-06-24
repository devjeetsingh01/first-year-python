
for i in range(10):
    print(i)
    if i == 5:
        break     # here break mila becuz 5 includes in range 10
else:
    print("done")


for a in range(7):
    print(a)
    if a == 9:
        break    # here break nahi mila becuz 9 is not included in range 7
else:
    print("Heheh you are done")

# IMPORTANT CONCEPT:
for i in range(5):
    print(i)          # here print(i) is written before break condition so 2 will be included 
    if i == 2:
        break
else:
    print("Done")


for i in range(1, 6):
    if i == 4:     # here break happen first then print so that's why 4 not included
        break
    print(i)
else:
    print("Done")


"""break stops the loop immediately at that line
👉 Anything after break in that iteration does NOT run"""

