```html
Lesson 15
```
Methods are functions that are "called on" values.
The index() list method returns the index of an item in the list.
The append() list method adds a value to the end of a list.
The insert() list method adds a value anywhere inside a list.
The remove() list method removes an item, specified by the value, from a list.
The sort() list method sorts the items in a list.
The sort() method's reverse=True keyword argument can make the sort() method sort in reverse order.
These list methods operate on the list "in place", rather than returning a new list value.

```html
Lesson 16
```
Strings can do a lot of the same things lists can do, but strings are immutable.
Immutable values like strings and tuples cannot be modified "in place".
Mutable values like lists can be modified in place.
Variables don't contain lists, they contain references to lists.
When passing a list argument to a function, you are actually passing a list reference.
Changes made to a list in a function will affect the list outside the function.
The \ line continuation character can be used to stretch Python instruction across multiple lines.

```python
# This is for the tuple example
>>> t = (1,2,3)
>>> t
(1, 2, 3)
>>> 
>>> 
>>> mylist = [1,2,3]
>>> type(t)
<class 'tuple'>
>>> 
>>> tup = ('a', 'a', 'b')
>>> 
>>> tup.count('a')
2
>>> 
>>> tup.index('a')
0
>>> 
>>> mylist[0] = 'New'
>>> 

# Tuple cannot be reassigned
>>> tup[0] = 'New'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    tup[0] = 'New'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> >>> t = (1,2,3)
>>> t
(1, 2, 3)
>>> 
>>> 
>>> mylist = [1,2,3]
>>> type(t)
<class 'tuple'>
>>> 
>>> tup = ('a', 'a', 'b')
>>> 
>>> tup.count('a')
2
>>> 
>>> tup.index('a')
0
>>> 
>>> mylist[0] = 'New'
>>> 
>>> tup[0] = 'New'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    tup[0] = 'New'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> 
>>> myset = set()
>>> type(myset)
<class 'set'>
>>> 
>>> myset.add(1)
>>> 
>>> myset
{1}
>>> 
>>> myset.add(2)
>>> 
>>> myset
{1, 2}
>>> 
>>> # looks like dict but it's not a dict because it doesn't have the key:value pair
>>> 
>>> myset.add(2)
>>> 
>>> myset
{1, 2}
>>> 
>>> mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
>>> 
>>> mylist
[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
>>> 
>>> newset = set(mylist)
>>> 
>>> newset
{1, 2, 3}

# Set is a collection of unique values
>>> myset = set()
>>> type(myset)
<class 'set'>
>>> 
>>> myset.add(1)
>>> 
>>> myset
{1}
>>> 
>>> myset.add(2)
>>> 
>>> myset
{1, 2}
>>> 
>>> # looks like dict but it's not a dict because it doesn't have the key:value pair
>>> 
>>> myset.add(2)
>>> 
>>> myset
{1, 2}

# Convert a list into Set

>>> mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
>>> 
>>> mylist
[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
>>> 
>>> newset = set(mylist)
>>> 
>>> newset
{1, 2, 3}
>>> 
```
Example for deepcopy of a list 

```python
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
```
List Comprehension 

```python
>>> mystr = 'hello'
>>> 
>>> newlist = []
>>> 
>>> for item in mystr:
	newlist.append(item)

	
>>> newlist
['h', 'e', 'l', 'l', 'o']
>>> 
>>> myanotherlist = [item for item in mystr]
>>> 
>>> myanotherlist
['h', 'e', 'l', 'l', 'o']
>>> 

>>> test = [x for x in 'a word']
>>> 
>>> test
['a', ' ', 'w', 'o', 'r', 'd']
>>> 

# operations can also be done inside the comprehension 
# it's a break of the operation during creation of the list
>>> numlist = [num**3 for num in [1,2,3]]
>>> 
>>> numlist
[1, 8, 27]
>>> 
>>> 
>>> numlist = [x**2 for x in range(0,11) if x%2==0]


>>> numlist
[0, 4, 16, 36, 64, 100]
>>> 
>>>
```
