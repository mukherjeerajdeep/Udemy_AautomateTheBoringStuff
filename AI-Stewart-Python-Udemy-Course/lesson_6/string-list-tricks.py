# Example of some operations
# Remmeber list is a reference not a variable

>>> list('Hello')
['H', 'e', 'l', 'l', 'o']
>>> 
>>> 
>>> name = 'rajdeep'
>>> 
>>> name[0]
'r'
>>> 
>>> name[:3]
'raj'
>>> 
>>> 
>>> 'deep' in name
True
>>> 


# String is immutable

>>> name = name[0:3] # it is possible 
>>> name 
'raj'
>>> 
>>> name[0] = 'K' # This is not possible
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    name[0] = 'K'
TypeError: 'str' object does not support item assignment
>>> 
>>> name = 'Zophie is a cat'
>>> 
>>> namenew = name[0:7] + ' the '  + name [12:]
>>> namenew
'Zophie  the cat'
>>>

# Deep copy example

>>> import copy
>>> 
>>> spam = [0,2,1,2,3]
>>> 
>>> cheese = copy.deepcopy(spam)
>>> 
>>> cheese
[0, 2, 1, 2, 3]
>>> 
>>> 
>>> spam
[0, 2, 1, 2, 3]
>>> 
>>> 
>>> spam[2] = 'Hello'
>>> 
>>> spam
[0, 2, 'Hello', 2, 3]
>>> 
>>> 
>>> cheese
[0, 2, 1, 2, 3]
>>> 
