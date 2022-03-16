# This is the new way of validation

import re

message = '''Call me at 415-233-4516 for my home or you can call me at my office 
at this number 334-566-9999'''

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
regex_match = phoneRegex.search(message)    # returns the first match
print(regex_match.group())

phoneRegex = re.compile(r'\d\d\d\-\d\d\d\-\d\d\d\d')
regex_match = phoneRegex.findall(message)   # returns the list of matches
print(regex_match)


