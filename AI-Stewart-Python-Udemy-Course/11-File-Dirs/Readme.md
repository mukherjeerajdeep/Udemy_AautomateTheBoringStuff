This is for the files and folders in the python 

In a file path, the folders and filename are separated by backslashes on Windows and forward slashes on Linux and Mac.
Use the `os.path.join()` function to combine folders with the correct slash.

The current working directory is the folder that any relative paths are relative to.
`os.getcwd()` will return the current working directory.
`os.chdir()` will change the current working directory.

Absolute paths begin with the root folder, relative paths do not.
The . folder represents "this folder", the .. folder represents "the parent folder".
`os.path.abspath()` returns an absolute path form of the path passed to it.
`os.path.relpath()` returns the relative path between two paths passed to it.
`os.makedirs()` can make folders.

`os.path.getsize()` returns a file's size.
`os.listdir()` returns a list of strings of filenames.
`os.path.exists()` returns True if the filename passed to it exists.
`os.path.isfile()` and os.path.isdir() return True if they were passed a filename or file path.


The `open()` function will return a file object which has reading and writing –related methods.
Pass `‘r'` (or nothing) to `open()` to open the file in read mode. Pass `‘w'` for write mode. Pass `‘a'` for append mode.
Opening a nonexistent filename in write or append mode will create that file.
Call `read()` or `write()` to read the contents of a file or write a string to a file.
Call `readlines()` to return a list of strings of the file's content.
Call `close()` when you are done with the file.


```python
import os

os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\14-Working-with-Excel-Pdf'

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
Use of `with open()` format to open a file and python will automatically will close it

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

**Store the data locally in Shelve module**

The `shelve` module can store Python values in a binary file.
The `shelve.open()` function returns a dictionary-like shelf value.

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

shelffile = shelve.open('mydata')
shelffile['cats']
['anime', 'zphoie', 'puka', 'humble', 'clio']
```

In python, it's always data are stored like `dictionaries`
like below the cats is a key and the right side is the values.

```python
cats = ['anime', 'zphoie', 'puka', 'humble', 'clio']

cats
['anime', 'zphoie', 'puka', 'humble', 'clio']
shelve <module 'shelve' from 'C:\\Python\\lib\\shelve.py'>

shelffile = shelve.open('mydata')
shelffile.keys <bound method Mapping.keys of <shelve.DbfilenameShelf object at 0x0000017876D7D810>>

shelffile.keys()
KeysView(<shelve.DbfilenameShelf object at 0x0000017876D7D810>)

list(shelffile.keys())
[]

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

Copying and moving the files and folders

```python
import shutil

shutil.copy(
    '/AI-Stewart-Python-Udemy-Course/11-File-Dirs/test.txt',
    '/AI-Stewart-Python-Udemy-Course/11-File-Dirs/test\\test.txt')
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test\\test.txt'

import os

os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs'

os.rmdir('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\delete')
The directory is not empty: 'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\delete'

import shutil

shutil.rmtree(
    'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\delete')
= RESTART: C: / Rajdeep_Mukherjee / Udemy_AautomateTheBoringStuff / AI - Stewart - Python - Udemy - Course / lesson_11_file_dirs / dryrun - delete - files - folders.py
dryrun - delete - files - folders.py
test - program - open - file.py

os.chdir(
    'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs')
os.listdir()
['copytree', 'dryrun-delete-files-folders.py', 'lesson30-recap.txt', 'lesson31-recap.txt', 'test',
 'test-program-open-file.py', 'test.txt']
 
```

```html
Lesson 33
```
`os.unlink()` will delete a file.
`os.rmdir()` will delete a folder (but the folder must be empty).
`shutil.rmtree()` will delete a folder and all its contents. Deleting can be dangerous, so do a "dry run" first.
`send2trash.send2trash()` will send a file or folder to the recycling bin.
Files have a name and a path. The root folder is the lowest folder.

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

[Relative and Absolute Path](https://automatetheboringstuff.com/2e/images/000057.jpg)
[File Folders](C:\Rajdeep_Mukherjee\The relative paths for folders and files in the working directory.jpg)

**Advanced Modules Exercise Solutions**
It's time to test your new skills, this puzzle project will combine multiple skills sets, including unzipping 
files with Python, using os module to automatically search through lots of files.

Your Goal
This is a puzzle, so we don't want to give you too much guidance and instead have you figure out things on your own.

There is a `.zip` file called '`unzip_me_for_instructions.zip`', unzip it, open the .txt file with Python, 
read the instructions and see if you can figure out what you need to do!

```python
import os
import re 

# Expecting that the python programs is running in the same path where the extracted_content is extracted.
for folder , sub_folders , files in os.walk(os.getcwd()+"\\extracted_content"):

    for file in files:
        file_path = folder+'\\'+file
        with open(file_path, 'r') as f:
            searcher = re.search(r'\d{3}-\d{3}-\d{4}', f.read())
            if searcher is not None:
                print(searcher.group())

OUTPUT
719-266-2837

```