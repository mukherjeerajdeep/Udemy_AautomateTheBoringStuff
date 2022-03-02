# Udemy_AautomateTheBoringStuff
Practice codes and lessons from the Book https://automatetheboringstuff.com/

Youtube link :
https://www.youtube.com/watch?v=_AEJHKGk9ns

```python
# Deep copy example

import copy

spam = [0,2,1,2,3]
cheese = copy.deepcopy(spam)
cheese
>>[0, 2, 1, 2, 3]


spam
>>[0, 2, 1, 2, 3]

spam[2] = 'Hello'
spam
>>>[0, 2, 'Hello', 2, 3]
cheese
>>>[0, 2, 1, 2, 3]

```


