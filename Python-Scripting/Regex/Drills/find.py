# Drill Regex

import re

## Create a regular expression that finds integers without size limit.
s = "sssgdds-8sfsfs"
print(re.search("[0-9]+", s))

## Create a regex that finds negative integers without size limit
s = "sssgdds-8sf7sfs"
print(re.search("-?[0-9]+", s))

## Create a regex that finds (positive or negative) integers without size limit.
s = "sssgdds-8s8-7fs9fs"
print(re.findall("-?[0-9]+", s))

# alternatively
# "r-" 's not a part of the regular expression syntax itself 
# but used to represent the  string as a raw string in Python
# treats backslash as literal xter not escape
pattern = r'-?\d+'
matches = re.findall(pattern, s)
print(matches)

## Capture all the numbers of the following sentence
text = "21 scouts and 3 tanks fought against 4,003 protestors, so the manager was not 100.00% happy."
pattern = r'-?\b\d+(?:,\d{3})*(?:\.\d+)?%?\b'
matches = re.findall(pattern, text)
print(matches)

##  Find all words that end with 'ly'.
text = "He had prudently disguised himself but was quickly captured by the police."
pattern = r'\b\w+ly\b'
matches = re.findall(pattern, text)
print(matches)