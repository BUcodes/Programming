# Management of directory paths
# Use the file path handling capability of os module

import os

# check available methods
help(os.path)

# check current absolute path
path = os.path.abspath('')
print(path)
print(type(path))

# check part of the path that consists of directories
os.path.dirname(path)

# to get the filename
os.path.basename(path)

# To add directory "text" to the path, we use join()
# on Windows it will automatically add \ between the 
# arguments of os.path.join, and on Linux it will add /
rep_text = os.path.join(path, "text")
print(rep_text)
     
# retrieve all the elements of a folder as a list
os.listdir("../")

# display all the elements of a folder as well as its child folders
folder_path = os.path.abspath("./")
print(folder_path)

for path, dirs, files in os.walk(folder_path):
    for filename in files:
        print(filename)



