# Task: License plate script

"""A license plate consists of 2 capital letters, a dash ('-'), 3 digits, a dash ('-') and finally 2 capital letters. 
Write a script to check that an input string is a license plate.
If it's correct, print "good". If it's not correct, print "Not good
"""

plate = input("Enter your license plate number: ")
pattern = r'[A-Z]{2}-\d{3}-[A-Z]{2}'
if re.match(pattern, plate):
    print("good")
else: 
    print("Not good")