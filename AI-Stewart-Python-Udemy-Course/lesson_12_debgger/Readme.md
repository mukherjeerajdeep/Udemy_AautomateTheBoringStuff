This is for the debugging console errors and examples

```python
>>> 
>>> import traceback
>>> try:
	raise Exception('This is the error message')
except:
	errorFile = open('error_log.txt', a)
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info was written error_log.txt')

	
Traceback (most recent call last):
  File "<pyshell#385>", line 2, in <module>
    raise Exception('This is the error message')
Exception: This is the error message

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#385>", line 4, in <module>
    errorFile = open('error_log.txt', a)
NameError: name 'a' is not defined
>>> try:
	raise Exception('This is the error message')
except:
	errorFile = open('error_log.txt', 'a')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info was written error_log.txt')

	
116
The traceback info was written error_log.txt
>>> 
>>> 
>>> os.getcwd()
Traceback (most recent call last):
  File "<pyshell#390>", line 1, in <module>
    os.getcwd()
NameError: name 'os' is not defined
>>> 
>>> 
>>> import os
>>> os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course'
>>> 
>>> os.chdir('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_12_debgger')
>>> 
>>> 
>>> os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_12_debgger'
>>> try:
	raise Exception('This is the error message')
except:
	errorFile = open('error_log.txt', 'a')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info was written error_log.txt')

	
116
The traceback info was written error_log.txt
>>> 
>>> 
>>> 
>>> assert False, 'This is another kind of error'
Traceback (most recent call last):
  File "<pyshell#405>", line 1, in <module>
    assert False, 'This is another kind of error'
AssertionError: This is another kind of error
>>> 
```