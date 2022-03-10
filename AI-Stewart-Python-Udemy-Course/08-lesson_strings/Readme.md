```html
Lesson 20
```
upper() and lower() return an uppercase or lowercase string.
isupper(), islower(), isalpha(), isalnum(), isdecimal(), isspace(), istitle() returns True or False if the string is that uppercase, lowercase, alphabetical letters, and so on.
startswith() and endswith() also return bools.
‘,'.join([‘cat', ‘dog']) returns a string that combines the strings in the given list.
‘Hello world'.split() returns a list of strings split from the string it's called on.
rjust() ,ljust(), center() returns a string padded with spaces.
strip(), rstrip(), lstrip() returns a string with whitespace stripped off the sides.
replace() will replace all occurrences of the first string argument with the second string argument.
Pyperclip has copy() and paste() functions for getting and putting strings on the clipboard.

```python
>>> spam = 'hello world'
>>> 
>>> spam.upper()
'HELLO WORLD'
>>> 
>>> 
>>> 
>>> 
>>> spam
'hello world'
>>> 
>>> 
>>> newspam = spam.upper()
>>> newspam
'HELLO WORLD'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ','.join(['cat', 'bat', 'rat'])
'cat,bat,rat'
>>> 
>>> ''.join(['cat', 'bat', 'rat'])
'catbatrat'
>>> 
>>> '\n\n'.join(['cat', 'bat', 'rat'])
'cat\n\nbat\n\nrat'
>>> 
>>> print('\n\n'.join(['cat', 'bat', 'rat']))
cat

bat

rat
>>> print('\n'.join(['cat', 'bat', 'rat']))
cat
bat
rat
>>>
>>> 
>>> 'My name is rajdeep'.split() # split based on the spaces
['My', 'name', 'is', 'rajdeep']
>>>
>>> 'My name is rajdeep'.split('m') # based on the letter 'm'
['My na', 'e is rajdeep']
>>> 
>>> print('My name is rajdeep'.split())
['My', 'name', 'is', 'rajdeep']
>>> 
>>> 
>>> for name in
SyntaxError: invalid syntax
>>> for name in 'My name is rajdeep'.split():
	print(name)

	
My
name
is
rajdeep
>>>
>>> 'hello'.rjust(10) # right justified 
'     hello'
>>> 
>>> 
>>> 'hello'.ljust(10) #left justified
'hello     '
>>>
>>> 'hello'.rjust(10, '*') # insert * when right justifying
'*****hello'
>>>
>>> 
>>> 'hello'.center(10) # centre justified
'  hello   '
>>> 'hello'.center(20, '*')
'*******hello********'
>>> 

```
Some more examples 

```python
>>> spam = 'hello world'
>>> 
>>> spam.upper()
'HELLO WORLD'
>>> 
>>> 
>>> 
>>> 
>>> spam
'hello world'
>>> 
>>> 
>>> newspam = spam.upper()
>>> newspam
'HELLO WORLD'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ','.join(['cat', 'bat', 'rat'])
'cat,bat,rat'
>>> 
>>> ''.join(['cat', 'bat', 'rat'])
'catbatrat'
>>> 
>>> '\n\n'.join(['cat', 'bat', 'rat'])
'cat\n\nbat\n\nrat'
>>> 
>>> print('\n\n'.join(['cat', 'bat', 'rat']))
cat

bat

rat
>>> print('\n'.join(['cat', 'bat', 'rat']))
cat
bat
rat
>>>
>>> 
>>> 'My name is rajdeep'.split() # split based on the spaces
['My', 'name', 'is', 'rajdeep']
>>>
>>> 'My name is rajdeep'.split('m') # based on the letter 'm'
['My na', 'e is rajdeep']
>>> 
>>> print('My name is rajdeep'.split())
['My', 'name', 'is', 'rajdeep']
>>> 
>>> 
>>> for name in
SyntaxError: invalid syntax
>>> for name in 'My name is rajdeep'.split():
	print(name)

	
My
name
is
rajdeep
>>>
>>> 'hello'.rjust(10) # right justified 
'     hello'
>>> 
>>> 
>>> 'hello'.ljust(10) #left justified
'hello     '
>>>
>>> 'hello'.rjust(10, '*') # insert * when right justifying
'*****hello'
>>>
>>> 
>>> 'hello'.center(10) # centre justified
'  hello   '
>>> 'hello'.center(20, '*')
'*******hello********'
>>>
>>> spam = 'hello'.rjust(10)
>>> 
>>> spam
'     hello'
>>> spam.strip()
'hello'
>>> 
>>> 
>>> 

```
String Formatting

```python
>>> 
>>> 'Hello %s please bring %s' % ('Alice', 'pie')
'Hello Alice please bring pie'
>>> 
```
