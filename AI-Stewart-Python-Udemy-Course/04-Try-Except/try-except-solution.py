def divBy42(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error : Divide by zero occured')

print(divBy42(2))
print(divBy42(10))
print(divBy42(0)) # This would return 'None' type/value as nothing to do here
print(divBy42(1))
