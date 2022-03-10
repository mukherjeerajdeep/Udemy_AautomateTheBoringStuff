This is for the files and folders in the python 

```html
Lesson 30
```
In a file path, the folders and filename are separated by backslashes on Windows and forward slashes on Linux and Mac.
Use the **os.path.join()** function to combine folders with the correct slash.

The current working directory is the oflder that any relative paths are relative to.
**os.getcwd()** will return the current working directory.
**os.chdir()** will change the current working directory.

Absolute paths begin with the root folder, relative paths do not.
The . folder represents "this folder", the .. folder represents "the parent folder".
**os.path.abspath()** returns an absolute path form of the path passed to it.
**os.path.relpath()** returns the relative path between two paths passed to it.
**os.makedirs()** can make folders.

**os.path.getsize()** returns a file's size.
**os.listdir()** returns a list of strings of filenames.
**os.path.exists()** returns True if the filename passed to it exists.
**os.path.isfile()** and os.path.isdir() return True if they were passed a filename or file path.

```html
Lesson 31
```
The **open()** function will return a file object which has reading and writing –related methods.
Pass ‘r' (or nothing) to open() to open the file in read mode. Pass ‘w' for write mode. Pass ‘a' for append mode.
Opening a nonexistent filename in write or append mode will create that file.
Call **read()** or **write()** to read the contents of a file or write a string to a file.
Call **readlines()** to return a list of strings of the file's content.
Call close() when you are done with the file.
The **shelve** module can store Python values in a binary file.
The **shelve.open()** function returns a dictionary-like shelf value.

```python
import os

os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\14-lesson_working_with_excel_pdf'

os.chdir('/AI-Stewart-Python-Udemy-Course/lesson_11_file_dirs')

hellofile = open('hello.txt')
hellofile.read()
'hello\nworld'

content = hellofile.read()
content
''

hellofile.close()

# need to reread it
hellofile = open('hello.txt')
content = hellofile.read()
content
'hello\nworld'

hellofile.close()

hellofile = open('hello.txt')
content = hellofile.readlines()
content
['hello\n', 'world']

# way of representation is different

hellofile.close()

hellofile = open('hello.txt', 'w')
hellofile.write('\nI am adding this line')
22

hellofile.close()

baconfile = open('hello.txt', 'a')

# **hellofile** is already closed as the, hence the error  

hellofile.write('\nI am adding this another line')
Traceback(most
recent
call
last):
File
"<pyshell#484>", line
1, in < module >
hellofile.write('\nI am adding this another line')
ValueError: I / O
operation
on
closed
file.

baconfile.write('\nI am adding this another line')
30

baconfile.writelines('\nI am adding this another line for wroitelines')

baconfile.close()
```

```python
# using binary Shelve file for temporary storing data

import shelve

shelve.open('mydata')
<shelve.DbfilenameShelf object at 0x000001787642CE50>

shelffile = shelve.open('mydata')

# store data into shelve file
shelffile['cats'] = ['anime', 'zphoie', 'puka'. 'humble', 'clio']
SyntaxError: invalid syntax
shelffile['cats'] = ['anime', 'zphoie', 'puka', 'humble', 'clio']

shelffile.close()

print('shelffile')
shelffile

print(mydata)
Traceback (most recent call last):
  File "<pyshell#514>", line 1, in <module>
    print(mydata)
NameError: name 'mydata' is not defined


shelffile = shelve.open('mydata')
shelffile['cats']
['anime', 'zphoie', 'puka', 'humble', 'clio']

# in python it's always data are stored like dictanaries

# like below the cats is a key and the right side is the values.
cats = ['anime', 'zphoie', 'puka', 'humble', 'clio']

cats
['anime', 'zphoie', 'puka', 'humble', 'clio']
shelve
<module 'shelve' from 'C:\\Python\\lib\\shelve.py'>

shelffile = shelve.open('mydata')
shelffile.keys
<bound method Mapping.keys of <shelve.DbfilenameShelf object at 0x0000017876D7D810>>
shelffile.keys()
KeysView(<shelve.DbfilenameShelf object at 0x0000017876D7D810>)


list(shelffile.keys())
[]

shelve.close()
Traceback (most recent call last):
  File "<pyshell#535>", line 1, in <module>
    shelve.close()
AttributeError: module 'shelve' has no attribute 'close'
shelffile.close()

shelffile = shelve.open('mydata')
list(shelffile.keys())
[]

shelffile['cats'] = ['anime', 'zphoie', 'puka', 'humble', 'clio']

list(shelffile.keys())
['cats']

shelffile.close()


shelffile = shelve.open('mydata')
list(shelffile.keys())
['cats']

shelffile.close()
```

```html
Lesson 32
```
Copying and moving the files and folders

```python
>> > import shutil
>> >
>> > shutil.copy(
    '/AI-Stewart-Python-Udemy-Course/11-lesson-file-dirs/test.txt',
    '/AI-Stewart-Python-Udemy-Course/11-lesson-file-dirs/test\\test.txt')
Traceback(most
recent
call
last):
File
"<pyshell#336>", line
1, in < module >
shutil.copy(
    '/AI-Stewart-Python-Udemy-Course/11-lesson-file-dirs/test.txt',
    '/AI-Stewart-Python-Udemy-Course/11-lesson-file-dirs/test\\test.txt')
File
"C:\Program Files\Python38\lib\shutil.py", line
415, in copy
copyfile(src, dst, follow_symlinks=follow_symlinks)
File
"C:\Program Files\Python38\lib\shutil.py", line
261, in copyfile
with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
    FileNotFoundError: [Errno 2]
No
such
file or directory: 'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test\\test.txt'
>> > shutil.copy(
    '/AI-Stewart-Python-Udemy-Course/11-lesson-file-dirs/test.txt',
    '/AI-Stewart-Python-Udemy-Course/11-lesson-file-dirs/test\\test.txt')
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test\\test.txt'
>> >
>> >
>> > shutil.copytree(
    '/AI-Stewart-Python-Udemy-Course/11-lesson-file-dirs/test',
    '/AI-Stewart-Python-Udemy-Course/11-lesson-file-dirs/copytree')
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\copytree'
>> >
>> >
>> >
>> > shutil.copy(
    '/AI-Stewart-Python-Udemy-Course/11-lesson-file-dirs/test\\test.txt',
    '/AI-Stewart-Python-Udemy-Course/11-lesson-file-dirs/copytree\\teststets.txt')
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\copytree\\teststets.txt'
>> >
>> >
>> >
>> > import os
>> >
>> > os..getcwd()
SyntaxError: invalid
syntax
>> > os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs'
>> >
>> >
>> > os.rmdir(
    'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\delete')
Traceback(most
recent
call
last):
File
"<pyshell#354>", line
1, in < module >
os.rmdir(
    'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\delete')
OSError: [WinError 145]
The
directory is not empty: 'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\delete'
>> >
>> > import shutil
>> >
>> > shutil.rmtree(
    'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\delete')
= RESTART: C: / Rajdeep_Mukherjee / Udemy_AautomateTheBoringStuff / AI - Stewart - Python - Udemy - Course / lesson_11_file_dirs / dryrun - delete - files - folders.py
dryrun - delete - files - folders.py
test - program - open - file.py
>> > os.chdir(
    'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs')
>> > os.listdir()
['copytree', 'dryrun-delete-files-folders.py', 'lesson30-recap.txt', 'lesson31-recap.txt', 'test',
 'test-program-open-file.py', 'test.txt']
>> >
>> > 
```

```html
Lesson 33
```
os.unlink() will delete a file.
os.rmdir() will delete a folder (but the folder must be empty).
shutil.rmtree() will delete a folder and all its contents.
Deleting can be dangerous, so do a "dry run" first.
send2trash.send2trash() will send a file or folder to the recycling bin.
Files have a name and a path.
The root folder is the lowest folder.

```python
import shutil

import os

os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs'

os.unlink('deletefile.txt')

os.rmdir('emptydir_test')
# However it will not able to delete the folder if there is anything inside

# Use shutil.rmtree() isntead
os.rmdir('testdir')
Traceback (most recent call last):
  File "<pyshell#571>", line 1, in <module>
    os.rmdir('testdir')
OSError: [WinError 145] The directory is not empty: 'testdir'

shutil.rmtree('testdir')
```

```html
Lesson 34
```
```html
[Relative and Absolute Path](https://automatetheboringstuff.com/2e/images/000057.jpg)
![Relative and Absolute Path](C:\Rajdeep_Mukherjee\The relative paths for folders and files in the working directory.jpg)
```
```python
with open('test.txt', mode='a') as f:
    f.write('\nWhat am i doing')
    
16

with open('test.txt', mode='r') as f:
    f.readline()
    
"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n"

with open('test.txt', mode='r') as f:
    f.readlines()
    
["Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n", 'What am i doing']

with open('test_new.txt', mode='w') as f:
    f.write('What am i doing')
    
15
```
