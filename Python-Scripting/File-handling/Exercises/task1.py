""" 
Task 1: Take the content of the data.txt file, capitalize all the words and write them in the file that you created
"""

filename = "./data/data.txt"
array = []
with open(filename, "r+") as input_file:
    content = input_file.read()
    capitalized_content = content.title()  # Capitalize words in the content
    array.append(capitalized_content)

# Print the contents of the array
print(array)














# Task: Put all the .txt files from the data/ directory into a variable. Then, copy the content of all the files from this variable into a file in data/ that you will name final.txt.