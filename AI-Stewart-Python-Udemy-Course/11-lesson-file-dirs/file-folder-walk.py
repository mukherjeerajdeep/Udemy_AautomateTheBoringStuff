import os
import shutil

# os.walk() returns the folder/subfolder/files structure
# so using it in a for-loop gives the recursive folders/files
for foldername, subfolders, filenames in os.walk(
        '/AI-Stewart-Python-Udemy-Course/lesson_11_file_dirs'):
    print('The folder is ' + foldername)
    print('The subfolderName is ' + str(subfolders))
    print('The filename is ' + str(filenames))

    for subfolder in subfolders:
        if 'test' in subfolder:
            print()
            print('!!! hey you have a folder named ' + subfolder)
            print()

    for file in filenames:
        if file.endswith('.py'):
            # shutil.copy() copies a file from src to dest.
            shutil.copy(os.path.join(foldername, file), os.path.join(foldername, file + '.backup'))

