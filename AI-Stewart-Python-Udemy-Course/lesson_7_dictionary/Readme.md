This is the examples for the dictionary

```doctest
Dictionaries contain key-value pairs. Keys are like a list's indexes.
Dictionaries are mutable. Variables hold references to dictionary values, not the dictionary value itself.
Dictionaries are unordered. There is no "first" key-value pair in a dictionary.
The keys(), values(), and items() methods will return list-like values of a dictionary's keys, vaues, and both keys and values, respectively.
The get() method can return a default value if a key doesn't exist.
The setdefault() method can set a value if a key doesn't exist.
The pprint module's pprint() "pretty print" function can display a dictionary value cleanly. The pformat() function returns a string value of this output.
```


```python
> >>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> 
>>> myCat
{'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> 
>>> 
>>> myCat.keys()
dict_keys(['size', 'color', 'disposition'])
>>> 
>>> 
>>> myCat.values()
dict_values(['fat', 'gray', 'loud'])
>>> 
>>> 
>>> 'size' in myCat # keys are checked 
True
>>> 'fat' in myCat # values are not checked, because default is keys
False
>>>
>>> 'fat' in myCat.values() # Now it's true
True
>>> 
>>> list(myCat.keys())
['size', 'color', 'disposition']
>>> 
>>> list(myCat.keys())
['size', 'color', 'disposition']
>>> 
>>> list(myCat.items())
[('size', 'fat'), ('color', 'gray'), ('disposition', 'loud')]
>>>

# get method knowhow

>>> eggs = {'name' : 'dogg', 'cspecies' : 'cat' , 'age' : 8}
>>> 
>>> eggs
{'name': 'dogg', 'cspecies': 'cat', 'age': 8}
>>> 
>>> eggs['color'] # as the key 'color' is not present hence it's an error
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    eggs['color']
KeyError: 'color'
>>> 
>> 
>>> eggs.get('age') # use of get() method can take default
8
>>> 
>>> eggs.get('color')
>>> 
>>> eggs.get('color', 0)
0
>>> 
>>>

# use of the condition in one line by setdefaults

>>> if 'color' not in eggs:
	eggs['color'] = 'black'

	
>>> eggs
{'name': 'dogg', 'cspecies': 'cat', 'age': 8, 'color': 'black'}
>>> 
>>>
>>> eggs = {'name' : 'dogg', 'cspecies' : 'cat' , 'age' : 8}
>>> 
>>> eggs.setdefault('color', 'black') # the setdefault makes sure that the key exists
'black'
>>> 
>>> eggs
{'name': 'dogg', 'cspecies': 'cat', 'age': 8, 'color': 'black'} 
>>> 
# setdefault() method doesn't do anything if the value is already set in the ditionary
>>> eggs.setdefault('color', 'orange') 
'black'
>>> 
>>> 

``` 


