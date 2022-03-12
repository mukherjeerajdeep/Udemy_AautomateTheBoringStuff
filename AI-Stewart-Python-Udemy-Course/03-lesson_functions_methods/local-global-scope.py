spam = 42  # global scope

def eggs():
    spam = 42  # local scope
    print(spam)

eggs()

# Example from the Jose Portila course
x = 50

def func():
    global x  # This is a label for the program which means to find out the global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)