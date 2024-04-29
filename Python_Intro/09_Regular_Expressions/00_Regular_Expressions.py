# What are regular expressions?

import re

# Very useful for finding things in a piece of text

# Python way:

string = 'Search inside of this text please'

print('Search' in string)

# Then why do we need regular expressions? 
# They are a little bit more powerful than the python way

a = re.search('this', string) # Returns a re.Match object

# Span(17,21) -> Means this starts on index 17, and ends on 21

print(a.end())   # prints 21 -> ending index
print(a.group()) # prints the "group" of patterns

a = re.search('ThIS', string) # Returns None

pattern = re.compile('Search')

pattern.search(string) # searches for the "pattern" value in string

b = pattern.findall(string)
c = pattern.fullmatch(string)

print(b)