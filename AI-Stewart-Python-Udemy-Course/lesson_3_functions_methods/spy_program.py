# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

# Exact match of the sequence
def spy_game(passedList):
    base = [0, 0, 7]

    for item in range(0, len(passedList) - 2):
        list_ = passedList[item:item + 3]
        if list_ == base:
            return True

    return False


print(spy_game([1, 2, 4, 0, 1, 7, 5]))
