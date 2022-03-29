Python advanced numbers

```python
hex(12)
'0xc'

oct(12)
'0o14'

bin(12)
'0b1100'

pow(2,4,3)
1

abs(2)
2

abs(-1)
1
```
Advanced Strings

```python
s.find('o')
4

s.center(20,'z')
'zzzzhello worldzzzzz'

s.split('e')
     
['h', 'llo world']

# in case we have this word
        
s = 'i have a pencil'
        
s.split(' ') # will split every space
        
['i', 'have', 'a', 'pencil']

for _ in s.split(' '):
        print(_)

        
i
have
a
pencil

s.partition('a')
        
('i h', 'a', 've a pencil')
```

Advanced Sets 
```python
s = set()
        
s.add(1)
        
s.add(2)
        
s
        
{1, 2}

s.add(2) # nothing will happen
        
s
        
{1, 2}


s.clear()
        
s
        
set()

s = {1,2,3}
        
sc = s.copy()
        
sc
        
{1, 2, 3}

s.add(5)
        
s
        
{1, 2, 3, 5}

sc
        
{1, 2, 3}

s.difference(sc)
        
{5}

s.difference_update(sc)
        
s
        
{5}

sc
        
{1, 2, 3}

sc.discard(2)
        
sc
        
{1, 3}


s = {1,2,3}
        
sc = {1,2,3,4}
        

s.intersection(sc)
        
{1, 2, 3}

s.intersection_update(sc)
        
s
        
{1, 2, 3}
sc
        
{1, 2, 3, 4}


s1 = {1,2}
        
s2 = {1,2,4}
        
s3 = {5}
        

s1.isdisjoint(s2)
        
False

s1.isdisjoint(s3)
        
True

s1.issubset(s2)
        
True

s1.issuperset(s2)
        
False

s1.symmetric_difference(s2)
        
{4}

s1.union(s2)
        
{1, 2, 4}

s1.update(s2)
        
s1
        
{1, 2, 4}

s2
        
{1, 2, 4}

```
Advanced Dictionary
```python

```
