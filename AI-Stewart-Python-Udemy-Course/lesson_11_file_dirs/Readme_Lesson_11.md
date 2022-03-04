This is for the files and folders in the python 

```python
>>> 
>>> 
>>> helloFile = open('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test.txt')
>>> 
>>> 
>>> helloFile.read()
'Etiam ut posuere arcu, in ornare quam. Etiam tincidunt mollis hendrerit. Ut eget molestie mauris, nec finibus sem. Morbi pellentesque, tortor quis luctus pretium, magna tellus laoreet quam, at mollis odio erat non nisl. Vestibulum aliquam vitae nunc et malesuada. Nullam vel sagittis nisl. Integer ac odio id dolor laoreet condimentum sed at nibh. Ut non sapien consectetur, dictum justo sit amet, pellentesque turpis.\n\nMauris diam tellus, gravida ut nulla at, luctus elementum mauris. Integer faucibus urna sed\nrisus rutrum, vel posuere nulla malesuada. Curabitur sagittis pretium justo accumsan pellentesque. Nullam s\nodales tortor eu nisl euismod tincidunt. Donec accumsan euismod sem, a tempus turpis accumsan volutpat.\nCurabitur varius diam eget vestibulum pretium. Interdum et malesuada fames ac ante ipsum primis\nin faucibus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia\ncurae; Curabitur porttitor sagittis leo, non semper neque placerat sed.\n\nIn facilisis eget augue ut ultrices. Nullam dui risus, imperdiet nec iaculis sed, rhoncus a arcu.\nPellentesque quis sapien mauris. Quisque congue tincidunt lectus et luctus. Duis fermentum ac mauris\nin commodo. Suspendisse massa neque, viverra sit amet nunc aliquam, laoreet elementum mi. In consectetur ex eu orci tincidunt facilisis.\n\nAliquam vulputate nisl sed leo scelerisque gravida. Proin augue ligula, efficitur et dignissim nec,\nefficitur non risus. Praesent sit amet lectus volutpat orci consectetur egestas eget eget metus.\nAenean semper id tellus eget ornare. Donec enim ante, convallis a volutpat non, bibendum feugiat enim.\n Ut ornare massa dictum est porta, nec malesuada ante eleifend. Mauris pretium id ex ac vulputate.\n Morbi urna nisi, imperdiet id iaculis vel, tristique vel augue.\n\nSuspendisse dignissim nibh vel sem porta, non pulvinar neque egestas. Praesent bibendum est a\nscelerisque luctus. Fusce lacus turpis, rhoncus sit amet fermentum non, scelerisque quis nibh.\nAenean nec rhoncus metus. Aenean fermentum efficitur arcu, in maximus mi tincidunt vitae. Praesent\nplacerat diam ipsum, ac faucibus turpis tempor sit amet. Proin tincidunt dignissim nibh tincidunt\nfringilla. Ut consequat eget tortor eu sagittis.'
>>> helloFile.close()
>>> 
>>> helloFile.read()
Traceback (most recent call last):
  File "<pyshell#304>", line 1, in <module>
    helloFile.read()
ValueError: I/O operation on closed file.
>>> helloFile = open('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test.txt')
>>> 
>>> 
>>> helloFile.read()
'Etiam ut posuere arcu, in ornare quam. Etiam tincidunt mollis hendrerit. Ut eget molestie mauris, nec finibus sem. Morbi pellentesque, tortor quis luctus pretium, magna tellus laoreet quam, at mollis odio erat non nisl. Vestibulum aliquam vitae nunc et malesuada. Nullam vel sagittis nisl. Integer ac odio id dolor laoreet condimentum sed at nibh. Ut non sapien consectetur, dictum justo sit amet, pellentesque turpis.\n\nMauris diam tellus, gravida ut nulla at, luctus elementum mauris. Integer faucibus urna sed\nrisus rutrum, vel posuere nulla malesuada. Curabitur sagittis pretium justo accumsan pellentesque. Nullam s\nodales tortor eu nisl euismod tincidunt. Donec accumsan euismod sem, a tempus turpis accumsan volutpat.\nCurabitur varius diam eget vestibulum pretium. Interdum et malesuada fames ac ante ipsum primis\nin faucibus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia\ncurae; Curabitur porttitor sagittis leo, non semper neque placerat sed.\n\nIn facilisis eget augue ut ultrices. Nullam dui risus, imperdiet nec iaculis sed, rhoncus a arcu.\nPellentesque quis sapien mauris. Quisque congue tincidunt lectus et luctus. Duis fermentum ac mauris\nin commodo. Suspendisse massa neque, viverra sit amet nunc aliquam, laoreet elementum mi. In consectetur ex eu orci tincidunt facilisis.\n\nAliquam vulputate nisl sed leo scelerisque gravida. Proin augue ligula, efficitur et dignissim nec,\nefficitur non risus. Praesent sit amet lectus volutpat orci consectetur egestas eget eget metus.\nAenean semper id tellus eget ornare. Donec enim ante, convallis a volutpat non, bibendum feugiat enim.\n Ut ornare massa dictum est porta, nec malesuada ante eleifend. Mauris pretium id ex ac vulputate.\n Morbi urna nisi, imperdiet id iaculis vel, tristique vel augue.\n\nSuspendisse dignissim nibh vel sem porta, non pulvinar neque egestas. Praesent bibendum est a\nscelerisque luctus. Fusce lacus turpis, rhoncus sit amet fermentum non, scelerisque quis nibh.\nAenean nec rhoncus metus. Aenean fermentum efficitur arcu, in maximus mi tincidunt vitae. Praesent\nplacerat diam ipsum, ac faucibus turpis tempor sit amet. Proin tincidunt dignissim nibh tincidunt\nfringilla. Ut consequat eget tortor eu sagittis.'
>>> 
>>> helloFile.readline()
''
>>> 
>>> 
>>> helloFile.close()
>>> 
>>> helloFile = open('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test.txt')
>>> 
>>> helloFile.readline()
'Etiam ut posuere arcu, in ornare quam. Etiam tincidunt mollis hendrerit. Ut eget molestie mauris, nec finibus sem. Morbi pellentesque, tortor quis luctus pretium, magna tellus laoreet quam, at mollis odio erat non nisl. Vestibulum aliquam vitae nunc et malesuada. Nullam vel sagittis nisl. Integer ac odio id dolor laoreet condimentum sed at nibh. Ut non sapien consectetur, dictum justo sit amet, pellentesque turpis.\n'
>>> 
>>> 
>>> helloFile.readlines()
['\n', 'Mauris diam tellus, gravida ut nulla at, luctus elementum mauris. Integer faucibus urna sed\n', 'risus rutrum, vel posuere nulla malesuada. Curabitur sagittis pretium justo accumsan pellentesque. Nullam s\n', 'odales tortor eu nisl euismod tincidunt. Donec accumsan euismod sem, a tempus turpis accumsan volutpat.\n', 'Curabitur varius diam eget vestibulum pretium. Interdum et malesuada fames ac ante ipsum primis\n', 'in faucibus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia\n', 'curae; Curabitur porttitor sagittis leo, non semper neque placerat sed.\n', '\n', 'In facilisis eget augue ut ultrices. Nullam dui risus, imperdiet nec iaculis sed, rhoncus a arcu.\n', 'Pellentesque quis sapien mauris. Quisque congue tincidunt lectus et luctus. Duis fermentum ac mauris\n', 'in commodo. Suspendisse massa neque, viverra sit amet nunc aliquam, laoreet elementum mi. In consectetur ex eu orci tincidunt facilisis.\n', '\n', 'Aliquam vulputate nisl sed leo scelerisque gravida. Proin augue ligula, efficitur et dignissim nec,\n', 'efficitur non risus. Praesent sit amet lectus volutpat orci consectetur egestas eget eget metus.\n', 'Aenean semper id tellus eget ornare. Donec enim ante, convallis a volutpat non, bibendum feugiat enim.\n', ' Ut ornare massa dictum est porta, nec malesuada ante eleifend. Mauris pretium id ex ac vulputate.\n', ' Morbi urna nisi, imperdiet id iaculis vel, tristique vel augue.\n', '\n', 'Suspendisse dignissim nibh vel sem porta, non pulvinar neque egestas. Praesent bibendum est a\n', 'scelerisque luctus. Fusce lacus turpis, rhoncus sit amet fermentum non, scelerisque quis nibh.\n', 'Aenean nec rhoncus metus. Aenean fermentum efficitur arcu, in maximus mi tincidunt vitae. Praesent\n', 'placerat diam ipsum, ac faucibus turpis tempor sit amet. Proin tincidunt dignissim nibh tincidunt\n', 'fringilla. Ut consequat eget tortor eu sagittis.']
>>> 
>>> 
>>> helloFile.read()
''
>>> helloFile.close()
>>> 
>>> 
>>> 
= RESTART: C:/Rajdeep_Mukherjee/Udemy_AautomateTheBoringStuff/AI-Stewart-Python-Udemy-Course/lesson_11_file_dirs/test-program-open-file.py
>>> 
= RESTART: C:/Rajdeep_Mukherjee/Udemy_AautomateTheBoringStuff/AI-Stewart-Python-Udemy-Course/lesson_11_file_dirs/test-program-open-file.py
Traceback (most recent call last):
  File "C:/Rajdeep_Mukherjee/Udemy_AautomateTheBoringStuff/AI-Stewart-Python-Udemy-Course/lesson_11_file_dirs/test-program-open-file.py", line 4, in <module>
    helloFile = open(path)
OSError: [Errno 22] Invalid argument: 'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\\nAI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test.txt'
>>> 
= RESTART: C:/Rajdeep_Mukherjee/Udemy_AautomateTheBoringStuff/AI-Stewart-Python-Udemy-Course/lesson_11_file_dirs/test-program-open-file.py
>>> 
= RESTART: C:/Rajdeep_Mukherjee/Udemy_AautomateTheBoringStuff/AI-Stewart-Python-Udemy-Course/lesson_11_file_dirs/test-program-open-file.py
>>> 
>>> 
>>> import shutil
>>> 
>>> shutil.copy('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test.txt', 'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test\\test.txt')
Traceback (most recent call last):
  File "<pyshell#336>", line 1, in <module>
    shutil.copy('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test.txt', 'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test\\test.txt')
  File "C:\Program Files\Python38\lib\shutil.py", line 415, in copy
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Program Files\Python38\lib\shutil.py", line 261, in copyfile
    with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test\\test.txt'
>>> shutil.copy('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test.txt', 'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test\\test.txt')
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test\\test.txt'
>>> 
>>> 
>>> shutil.copytree('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test' , 'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\copytree')
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\copytree'
>>> 
>>> 
>>> 
>>> shutil.copy('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\test\\test.txt' , 'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\copytree\\teststets.txt')
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\copytree\\teststets.txt'
>>> 
>>> 
>>> 
>>> import os
>>> 
>>> os..getcwd()
SyntaxError: invalid syntax
>>> os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs'
>>> 
>>> 
>>> os.rmdir('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\delete')
Traceback (most recent call last):
  File "<pyshell#354>", line 1, in <module>
    os.rmdir('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\delete')
OSError: [WinError 145] The directory is not empty: 'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\delete'
>>> 
>>> import shutil
>>> 
>>> shutil.rmtree('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs\\delete')
= RESTART: C:/Rajdeep_Mukherjee/Udemy_AautomateTheBoringStuff/AI-Stewart-Python-Udemy-Course/lesson_11_file_dirs/dryrun-delete-files-folders.py
dryrun-delete-files-folders.py
test-program-open-file.py
>>> os.chdir('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_11_file_dirs')
>>> os.listdir()
['copytree', 'dryrun-delete-files-folders.py', 'lesson30-recap.txt', 'lesson31-recap.txt', 'test', 'test-program-open-file.py', 'test.txt']
>>> 
>>> 
```