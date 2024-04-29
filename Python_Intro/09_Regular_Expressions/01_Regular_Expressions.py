# Now, 00_Regular_Expressions.py are simple but re have more than that
# Search the special sets of regular expressions

import re

# [a-zA-Z] -> A character in range of a-z or A-Z

# It's kinda complicated 

# RegEx101

# What are use cases?
# A user inputs something, we can validate it's in the correct form using re

email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

invalid_email = 'tyler\'semail@yahoo.com'
valid_email = 'tyleremail@yahoo.com'

a = email_pattern.search(invalid_email)
b = email_pattern.search(valid_email)

print(a) # None -> string is not a valid email
print(b) # Finds a matching object, thus a valid email