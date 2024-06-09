# Data scraping: Working with xml files
# XML-eXtensible Markup Language is a language that is written using tags
#  It is simple,extensible and configurable so that any type of data can be described


from lxml import etree

filename = "files/data.xml"
with open(filename, "r") as file:
  print(file.read())

# define the source document
tree = etree.parse(filename)

# identify path to the tag to get to the "user" information
for user in tree.xpath("/users/user/name"):
  # I only want to display the content (.text) of the `/users/user/name` tags
  print(user.text)

name = tree.xpath("/users/user/name")[0].text
print(name)

# display the attributes of the tags that store the information
tree = etree.parse(filename)
for user in tree.xpath("/users/user"):
    print(user.get("data-id"))

# display only users whose job is Veterinary
tree = etree.parse(filename)
for user in tree.xpath("/users/user[job='Veterinary']/name"):
    print(user.text)


