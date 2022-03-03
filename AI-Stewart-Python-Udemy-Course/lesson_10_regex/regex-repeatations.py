import re

message = 'The Batman and Batwoman went together with the Batbaby'

batRegex = re.compile(r'Bat(man|woman)')  # matches bat man or woman
search = batRegex.search(message)
print(search.group())

batRegex = re.compile(r'Bat(wo)?man')  # matches 'wo' either 0 or 1 times, optional kind
search = batRegex.search(message)
print(search.group())
searchAgain = batRegex.search(
    "There is a Batwowowowowman")  # returns 'None' type and there can't be any group() method in "None" type
print(searchAgain.group())
