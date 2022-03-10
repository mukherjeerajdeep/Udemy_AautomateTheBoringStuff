# function from the map() example
def square(number):
    return number ** 2


print(square(2))

# will transform into lambda, this will complain and ask us to use it inside
# the def, why ? because lambda is an anonymous function expression, so using
# it like that makes no sense.
num_ = lambda num: num ** 2
print(num_(5))


# so using the map example from previous
# Another example for the map usage with list
def using_map_list(numList):
    return list(map(lambda num: num ** 2, numList))


myList = [1, 2, 3, 4]
print(using_map_list(myList))
print(myList)


# applying the filer with lambda expression
def using_filter(listNum):
    return list(filter(lambda num: num % 2 == 0, listNum))


myList = [6, 7, 8, 9]
print(using_filter(myList))
print(myList)


def doNothing():
    print("What's up")


def using_nothing():
    map(lambda a, b: (
        b - a if a <= b else
        a * b
    )
        , [1, 2, 3])

using_nothing()