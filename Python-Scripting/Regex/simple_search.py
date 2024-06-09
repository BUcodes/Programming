# REGEX- Regular Expression
# It is a powerful tool to check, extract, modify the content of a variable as desired

import re

#using re.search to search for matches
pattern = "[ ]"
string = "I am fine ! There are still 6 months left :()"

# if matches are found, returns a `MatchObject` 
# otherwise returns `None`.
print(re.search(pattern, string))

# using re.split
# Cuts the string according to the occurrence of the pattern.
print(re.split(pattern, string))

# using RE.MATCH. RE.COMPLILE
# If the answer is not None, it means the match matches
# Can be written in two different syntaxes:
# First syntax
print(re.match("GR(.)?Y", "GREY"))

# Second syntax
pattern = "GR(.)?Y"
string = "GREY"
result = re.match(pattern, string)
print(result)

# alternatively
compiled = re.compile(pattern)
result = compiled.match(string)
print(result)

#  So in a loop the second syntax is nicer
pattern = "GR(.)?Y"
compiled = re.compile(pattern)
l = ["GREY 'S", "GRAY", "GREYISH", "A GREY"]

for elem in l:
    result = compiled.match(elem)
    print(elem, result)


## using RE.FINDALL- searches for specific expression in a string

# unique element (.)? between GR and Y
print(re.findall("GR(.)?Y", "GREY"))

# Ditto for two characters to be found
re.findall("G(.)?(.)?Y", "GREY")

# Only numbers
# "+" indicates 1 or more characters
print(re.findall("([0-9]+)", "Hello I live on the 7th floor of 220 street of sims"))

# only words
print(re.findall("([A-z]+)", "Hello I live on the 7th floor of 220 street of sims"))

# How to check that the entered string is that of a number?
number = input("Your number : ")
if re.match("^[0-9]+$", number):
    print("The string entered is a number.")
else:
    print("The string entered is NOT a number.")

# alternatively
compiled = re.compile("^[0-9]+$")
if compiled.search(number) is not None:
    print("The string entered is a number.")
else:
    print("The string entered is NOT a number")
