This is for the debugging console errors and examples

You can raise your own exceptions: **raise Exception(‘This is the error message.')**
You can also use assertions: assert condition, ‘Error message'
Assertions are for detecting programmer errors that are not meant to be recovered from. 
User errors should raise exceptions.

```python
>> >
>> > import traceback
>> > try:
    raise Exception('This is the error message')
except:
    errorFile = open('error_log.txt', a)
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')

Traceback(most
recent
call
last):
File
"<pyshell#385>", line
2, in < module >
raise Exception('This is the error message')
Exception: This is the
error
message

During
handling
of
the
above
exception, another
exception
occurred:

Traceback(most
recent
call
last):
File
"<pyshell#385>", line
4, in < module >
errorFile = open('error_log.txt', a)
NameError: name
'a' is not defined
>> > try:
    raise Exception('This is the error message')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')

116
The
traceback
info
was
written
error_log.txt
>> >
>> >
>> > os.getcwd()
Traceback(most
recent
call
last):
File
"<pyshell#390>", line
1, in < module >
os.getcwd()
NameError: name
'os' is not defined
>> >
>> >
>> > import os
>> > os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course'
>> >
>> > os.chdir('/AI-Stewart-Python-Udemy-Course/12-lesson_debgger')
>> >
>> >
>> > os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\12-lesson_debgger'
>> > try:
    raise Exception('This is the error message')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')

116
The
traceback
info
was
written
error_log.txt
>> >
>> >
>> >
>> > assert False, 'This is another kind of error'
Traceback(most
recent
call
last):
File
"<pyshell#405>", line
1, in < module >
assert False, 'This is another kind of error'
AssertionError: This is another
kind
of
error
>> > 
```

The logging module lets you display logging messages.

Log messages create a "breadcrumb trail" of what your program is doing.
After calling **logging.basicConfig()** to set up logging, call logging.debug(‘This is the message') to create a log message.

When done, you can disable the log messages with logging.disable(logging.CRITICAL)
Don't use print() for log messages: It's hard to remove the mall when you're done debugging.

The five log levels are: DEBUG, INFO, WARNING, ERROR, and CRITICAL.
You can also log to a file instead of the screen with the filename keyword argument in the logging.basicConfig() function.



