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
