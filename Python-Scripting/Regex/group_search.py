# REGEX- Group Search
# group search functionality of regex is quite powerful

import re

# Example 1
m = re.search(
    "Welcome to (?P<w>\w+) ! You are (?P<d>\d+) years old ?", 
    "Welcome to Olivier ! You are 32 years old ?",
)

if m:
  print("Name:", m.group("w"))
  print("Age:", m.group("d"))
else:
  print("No match found.")

# Example 2
m = re.search(
  r"^(?P<who>\w*)[.]?(?P<who2>\w*)@(?P<operator>\w+)[.](?P<zone>\w+$)",
  "audrey.boulevart@benextcomapgny.com",
)

if m is not None:
  print(m.group("who"))
  print(m.group("who2"))
  print(m.group("operator"))
  print(m.group("zone"))
else:
  print("No match found.")


# Alternatively
mail = "audrey.boulevart@benextcomapgny.com"
splitMail = mail.replace(".", " ").split("@").copy()

firstName = []
name = []
ope = []
zone = []

firstName.append(splitMail[0].split()[0])
name.append(splitMail[0].split()[-1])
ope.append(splitMail[1].split()[0])
zone.append(splitMail[1].split()[-1])

print(firstName, name, ope, zone)
