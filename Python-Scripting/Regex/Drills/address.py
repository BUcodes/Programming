# Task: Address IPV4 Script

"""An IPv4 address is composed of 4 numbers between 0 and 255 separated by '.'
Write a script to verify that a string entered is that of an IPv4 address.
"""

ip = input("Enter your IP address :")
pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
if re.match(pattern, ip):
    print("good")
else:
    print("Not good")

# write a script that checks for valid email address
email = input("Enter your email address :")
pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
if re.match(pattern, email):
    print("good")
else:
    print("Not good")

# script that verifies the password which has to contain at least 6 characters.
password = input("Enter your password :")
pattern = r'^.{6,}$'
if re.match(pattern, password):
    print("good")
else:
    print("Not good")

# a password with 6 characters, at least one lowwer, upper, number, and special character.
password = input("Enter your password :")
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,}$'
if re.match(pattern, password): 
    print("good")
else:
    print("Not good")



