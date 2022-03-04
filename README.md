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

```text
Files have a name and a path.
The root folder is the lowest folder.
In a file path, the folders and filename are separated by backslashes on Windows and forward slashes on Linux and Mac.
Use the os.path.join() function to combine folders with the correct slash.
The current working directory is the oflder that any relative paths are relative to.
os.getcwd() will return the current working directory.
os.chdir() will change the current working directory.
Absolute paths begin with the root folder, relative paths do not.
The . folder represents "this folder", the .. folder represents "the parent folder".
os.path.abspath() returns an absolute path form of the path passed to it.
os.path.relpath() returns the relative path between two paths passed to it.
os.makedirs() can make folders.
os.path.getsize() returns a file's size.
os.listdir() returns a list of strings of filenames.
os.path.exists() returns True if the filename passed to it exists.
os.path.isfile() and os.path.isdir() return True if they were passed a filename or file path.
```

