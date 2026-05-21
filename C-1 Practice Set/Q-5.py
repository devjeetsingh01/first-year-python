# step 1 import karo os ko
import os
# specify the directory path you want to list
path = '/'
# list all files and dorectories in specific path
contents = os.listdir(path)
# Print eah file and directory name
for items in contents:
    print(items)