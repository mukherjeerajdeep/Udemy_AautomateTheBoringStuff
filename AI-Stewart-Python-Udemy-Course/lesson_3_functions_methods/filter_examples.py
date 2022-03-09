# Filter is a method that can be applied on an iterable
import pprint


# function from the map() example
def square(number):
    return number ** 2


# Simple function to return True/False
def check_even(num):
    return num % 2 == 0


# applying the filter, returns a filtered list based on the function passed
def using_filter(listNum):
    return list(filter(check_even, listNum))


def using_map_filter(listNum):
    return list(filter(check_even, map(square, listNum)))


mylist = [1, 2, 3, 4]
print(using_filter(mylist))
print(mylist)

pprint.pprint("Anything Can be applied")
print(using_map_filter(mylist))
