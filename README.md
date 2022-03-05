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

Files and Directories


```commandline
C:\Rajdeep_Mukherjee\Udemy_AautomateTheBoringStuff\AI-Stewart-Python-Udemy-Course\lesson_13_websrcapping>c:\Python\python.exe -m pip install --upgrade pip


C:\Rajdeep_Mukherjee\Udemy_AautomateTheBoringStuff\AI-Stewart-Python-Udemy-Course\lesson_13_websrcapping>c:\Python\python.exe -m pip install beautifulsoup4
Collecting beautifulsoup4

C:\Rajdeep_Mukherjee\Udemy_AautomateTheBoringStuff\AI-Stewart-Python-Udemy-Course\lesson_13_websrcapping>c:\Python\python.exe -m pip install openpyxl
Collecting openpyxl
  
C:\Rajdeep_Mukherjee\Udemy_AautomateTheBoringStuff\AI-Stewart-Python-Udemy-Course\lesson_13_websrcapping>c:\Python\python.exe -m pip install selenium
Collecting selenium
  
C:\Rajdeep_Mukherjee\Udemy_AautomateTheBoringStuff\AI-Stewart-Python-Udemy-Course\lesson_13_websrcapping>c:\Python\python.exe -m pip install pyPDF2
Collecting pyPDF2 

C:\Rajdeep_Mukherjee\Udemy_AautomateTheBoringStuff\AI-Stewart-Python-Udemy-Course\lesson_13_websrcapping>c:\Python\python.exe -m pip install python-docx
Collecting python-docx
```
