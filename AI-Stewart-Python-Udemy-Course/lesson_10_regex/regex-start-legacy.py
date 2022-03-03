# This is the old way of validation
def isPhoneNumber(text): # 415-231-576
    if len(text) != 12:
        return False
    for i in range(0, 3): # 415
        if not text[i].isdecimal():
            return False
    if text[3] != '-':  # check '-'
        return False
    for i in range(4, 7): # check 231
        if not text[i].isdecimal():
            return False
    if text[7] != '-': # check the next '-'
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


# print(isPhoneNumber('415-223-2142'))
# print(isPhoneNumber('415-ABC-214'))
# print(isPhoneNumber('415-223-2'))

message = '''Call me at 415-233-4516 for my home or you can call me at my office 
at this number 334-566-9999'''

foundNumber = False

for i in range(len(message)):  # each character will be an element of the loop
    chunk = message[i:i+12]  # it will slice out next character at 1 and +12 so until 13 characters for evaluation
    if isPhoneNumber(chunk):
        foundNumber = True
        print("Phone number found " + chunk)

if not foundNumber:
    print("Phone number not found in message")