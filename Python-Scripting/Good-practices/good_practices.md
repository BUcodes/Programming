# Good Practices in Programming

Some rules guide how we code. They make teamwork, sharing, and productivity much easier.

Python codes are often written in line with some conventions, some of which have become unanimously used. Here is a summary of the most important rules.

## PEP 8
**PEP 8** (for Python Extension Proposal) is a set of rules that allows to homogenize the code and to apply good practices. It provides rules and conventions to make reading easier and thus less stressed and more productive. The advantage of PEP 8 is that it makes the code more attractive.

### Indentation
The code must be indented by 4 characters. For example:

👌 Good :
```py
def indent():
    my_var = "Use 4 characters for indent"
```

❌ Bad :
```py
def indent():
  my_var = "Use 4 characters for indent"
```

### Code layout
Use 79 characters per line, no more. This convention is adopted to improve code readability and maintainability. For example:

👌 Good :
```py
def my_function(
    context, width, height, size=10000, color="black", emphasis=None, highlight=0
):
    pass
```

❌ Bad :
```py
def my_function(context, width, height, size=10000, color="black", emphasis=None, highlight=0):
    pass
```

### Import
Imports are declared at the beginning of the script or in _function_ after the docstring. Allow one line per import. Separate imports. First you have to put the modules that are internal to Python. Then you have to import the third party libraries like `bs4`, `numpy`... Then you import your own modules. Each part of the modules must be separated by a line that spaces them out.

👌 Good :
```py
import os  # Standard library imports first
import sys  # alphabetical

import some_third_party_lib  # 3rd party stuff next
import some_third_party_other_lib  # alphabetical

import local_stuff  # local stuff last
import more_local_stuff
```

❌ Bad :
```py
import local_stuff, more_local_stuff, dont_import_two, modules_in_one_line  # IMPORTANT!
import os, sys
import some_third_party_lib
```

### Spaces 

Operators must be surrounded by spaces. For example:

👌 Good :
```py
name = 'Batman'
color == 'black'
1 + 2
❌ Bad :

name='name'
color=='black'
1+2
```

❌ Bad :
```py
name='name'
color=='black'
1+2
```

However, there are two **(2) notable exceptions** viz:

First, mathematical operators with the highest priority are grouped together to distinguish groups:

👌 Good :
```py
a = x*2 - 1
b = x*x + y*y
c = (a+b) * (a-b)
```

Second, the `=` sign in argument declaration and parameter passing:

👌 Good :
```py
def my_function(arg='value'):
    pass
 
result = my_fonction(arg='value')
```

There is no space inside parentheses, brackets or braces.

👌 Good :
```py
2 * (3 + 4)
def function(arg='valeur'):
{str(x): x for x in range(10)}
val = dic['key']
```

❌ Bad :
```py
2 * ( 3 + 4 ) 
def function( arg= 'valeur' ):

{ str( x ): x for x in range( 10 )}

val = dic  ['key']
```

Don't put a space before colons and commas, but you do afterwards.

👌 Good :

```py
def my_function(arg1='valeur', arg2=None):
 
dic = {'a': 1}
```

❌ Bad :

```py
def my_function(arg='value' , arg2=None) :
 
dico = {'a' : 1}
```

### Docstrings

These are used to define a particular program or define a particular function. They include single and multi-line docstrings. Examples:

```py
def exam():
    """This is single line docstring"""

    """This is
    a
    multiline comment"""
```

### Naming conventions

Naming conventions make programs less complex and more readable. Here are few conventions that can be followed easily:

Variable, function and module : Use snake_case.

👌 Good :
```py
my_variable = 'Hello'

def my_function(element):
    pass
```

❌ Bad :
```py
myVariable = 'Hello'
MyVariable = 'Hello'

def myFunction(element):
    pass
```

Class: Use PascalCase

👌 Good :
```py
class MyClass:
```

❌ Bad :
```py
class my_class:
```

## Summary


**Import:**
```py
import os  # STD lib imports first
import sys  # alphabetical

import some_third_party_lib  # 3rd party stuff next
import some_third_party_other_lib  # alphabetical

import local_stuff  # local stuff last
import more_local_stuff
import dont_import_two, modules_in_one_line  # IMPORTANT!
from pyflakes_cannot_handle import *  # and there are other reasons it should be avoided # noqa

# Using # noqa in the line above avoids flake8 warnings about line length!
```

**Column limit:**
```py
# some examples of how to wrap code to conform to 79-columns limit:
    def __init__(self, width, height, color="black", emphasis=None, highlight=0):
        if (
            width == 0
            and height == 0
            and color == "red"
            and emphasis == "strong"
            or highlight > 100
        ):
            raise ValueError("sorry, you lose")
        if width == 0 and height == 0 and (color == "red" or emphasis is None):
            raise ValueError("I don't think so -- values are %s, %s" % (width, height))
        Blob.__init__(self, width, height, color, emphasis, highlight)

    # empty lines within method to enhance readability; no set rule
    short_foo_dict = {
        "loooooooooooooooooooong_element_name": "cat",
        "other_element": "dog",
    }

    long_foo_dict_with_many_elements = {"foo": "cat", "bar": "dog"}

    # 1 empty line between in-class def'ns
    def foo_method(self, x, y=None):
        """Method and function names are lower_case_with_underscores.
        Always use self as first arg.
        """
        pass

    @classmethod
    def bar(cls):
        """Use cls!"""
        pass


# a 79-char ruler:
# 34567891123456789212345678931234567894123456789512345678961234567897123456789
```

**Other naming conventions:**
```
snake_case
MACRO_CASE
camelCase
CapWords
```
