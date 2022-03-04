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
if searchAgain is not None:
    print(searchAgain.group())
print("Error")

batRegex = re.compile(r'Bat(wo)+man')  # matches 'wo' one or more times, not optional
searchAgain = batRegex.search(
    "There is a Batwowowowoman")  # returns 'None' type and there can't be any group() method in "None" type
print(searchAgain.group())

phoneRegex = re.compile(r'((\d{3}-)?(\d{3}-)(\d{4})(,)?){3}')  # matches 415-555-1234, 555-1234, 211-666-1901
phoneSearch = phoneRegex.search("I have the numbers as this 415-555-1234, 555-1234, 211-666-1901 so call me")

if phoneSearch is not None:
    print(phoneSearch.group())
print("Error")
