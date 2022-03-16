Example of the try-Except with else block 

```python
try:
    result = 10 + 10
except:
    print('Please add correct number')
else:
    print('Add goes well')
    print(result)

    
Add goes well
20

try:
    result = 10 + '10'    
except:
    print('Please add correct number')
else:
    print('Add goes well')
    print(result)

    
Please add correct number

# Another example with opening file and finally

try:
    f = open('testfile', 'w')
    f.write('Write a test file')
except TypeError:
    print('TypeError occured')
except IOError:
    print('IOError occured')
finally:
    print('I will always run')

    
17
I will always run

# Now when we open a file and try to write it
try:
    f = open('testfile', 'r')
    f.write('Write a test file')
except TypeError:
    print('TypeError occured')
except IOError:
    print('IOError occured')
finally:
    print('I will always run')

    
IOError occured
I will always run
```
Finally, will always execute whether the `try` is executed or the `except` is executed

```python
def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            break
        finally:
            print("Finally, I executed!")
        print(val)

        
askint()
Please enter an integer: 20
Yep that's an integer!
Finally, I executed!


askint()
Please enter an integer: FAT
Looks like you did not enter an integer!
Finally, I executed!
Please enter an integer: '20'
Looks like you did not enter an integer!
Finally, I executed!
Please enter an integer: 100
Yep that's an integer!
Finally, I executed!
```