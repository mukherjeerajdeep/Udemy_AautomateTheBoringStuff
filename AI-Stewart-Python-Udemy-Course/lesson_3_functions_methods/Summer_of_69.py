# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of
# numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(listOfData):
    # If the list is empty then return zero
    # if len(listOfData) == 0:
    #     return 0

    sumTotal = 0
    isFlagSet = False

    for num in listOfData:
        if num != 6 and not isFlagSet:  # if '6' not found and Flag is not set, then sum up
            sumTotal += num
        else:
            isFlagSet = True  # isFlagSet to ON as soon as '6' is found in list

        if isFlagSet and num == 9:  # watch out for '9' to come because 6 was already found
            isFlagSet = False

    return sumTotal


# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))
print(summer_69([]))  # -> 0
# print(summer_69([1, 2, 6, 1, 9, 3, 1, 6, 1, 1, 9, 1, 1]))  # -> 9
