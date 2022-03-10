# Explanation of the map/filter and the lambda functions

# Simple function to make squares
def square(number):
    return number ** 2


# map calls the functions over the iterator
def using_map(numList):
    for item in map(square, numList):
        print(item)


# Another example for the map usage with list
def using_map_list(numList):
    return list(map(square, numList))


using_map([1, 2, 3, 4])
print(using_map_list([1, 2, 3, 4]))
