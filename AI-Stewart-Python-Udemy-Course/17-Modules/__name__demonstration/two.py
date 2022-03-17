# Two.py file
import one

def func():
    pass

print("Top level for two.py")
one.func()  # Function call for the one.py

if __name__ == '__main__':
    print('Two.py is being run directly!')
else:
    print('Two.py is being imported!')
