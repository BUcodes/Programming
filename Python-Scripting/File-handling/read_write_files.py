# File manipulation: Read and write files

# open() function
# this function takes file path as first parameter and type of opening as second 
# i.e reading "r" or writing mode "w"
# to read the previous data and add to it, you should use "r+

filename = "./data/data.txt"
my_file = open(filename, "r")
print(my_file.read())
# file must be closed once instruction is carried out
my_file.close()    

# open file without closing as best practice
with open(filename, "r") as my_file:
    print(my_file.read())
    
# put content in list form
with open(filename, "r") as my_file:
    content = my_file.read()
    print(content.split(" "))
    
# Write in a file
file = open(filename, "w")
file.write("Hi everyone, I'm adding sentences to the file !")
file.close()