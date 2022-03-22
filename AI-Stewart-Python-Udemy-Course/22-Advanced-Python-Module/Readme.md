

```python
from collections import Counter
mylist = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4]

# Counter counts the number of repetitions inside a list
Counter(mylist)
Counter({1: 6, 2: 6, 3: 6, 4: 2})

Counter('rajdeep')
Counter({'e': 2, 'r': 1, 'a': 1, 'j': 1, 'd': 1, 'p': 1})

# It counts the value as key and number of occurances as value
sentence = "How mnay times i have written the same lettere"
Counter(sentence)
Counter({' ': 8, 'e': 8, 't': 6, 'm': 3, 'a': 3, 'i': 3, 'w': 2, 'n': 2, 's': 2, 'h': 2, 'r': 2, 'H': 1, 'o': 1, 'y': 1, 'v': 1, 'l': 1})

# default dictionary is a special dictionary than in Python
from collections import defaultdict

d = {'a':10}

# lets call a wrong key
d['d']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    d['d']
KeyError: 'd'

# this will make noise in code, hence to use a default ditionaru
d= defaultdict(lambda:0)

# now assign values and keys to d
d['key'] = 100

d['key']
100

# Now try a value which is not present inside the dictionary
d['wrongkey']
0

# demonstrate named tuple
mytup = (10,20,30)

mytup.index(0)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    mytup.index(0)
ValueError: tuple.index(x): x not in tuple

mytup.index(10)
0

mytup[0]
10

from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sammy = Dog(12, 'husky', 'Ruth')

sammy.
SyntaxError: invalid syntax
sammy.age
12


import datetime

mytime = datetime.time(2,20)
mytime.minute
20

mytime.hour
2
print(mytime)
02:20:00

type(mytime)
<class 'datetime.time'>

today = datetime.date.today()
print(today)
2022-03-20

today.year
2022

today.month
3

today.ctime()
'Sun Mar 20 00:00:00 2022'






import pdb

x = [1,2,3]
y =2

z = 3

result_one = y+z
pdb.set_trace()
--Call--
> c:\python\lib\idlelib\rpc.py(614)displayhook()
-> def displayhook(value):
(Pdb) x+y
*** NameError: name 'x' is not defined
(Pdb) z
*** NameError: name 'z' is not defined
(Pdb) x = [1,2,3]
(Pdb) y =2
(Pdb) z = 3
(Pdb) 
(Pdb) x+y
*** TypeError: can only concatenate list (not "int") to list
(Pdb) 
*** TypeError: can only concatenate list (not "int") to list
(Pdb) y+z
5
(Pdb) 
5
(Pdb) q
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    pdb.set_trace()
bdb.BdbQuit


```