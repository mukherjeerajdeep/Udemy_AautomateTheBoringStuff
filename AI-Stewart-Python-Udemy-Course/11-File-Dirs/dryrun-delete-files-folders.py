import os

os.chdir('/AI-Stewart-Python-Udemy-Course/lesson_11_file_dirs')

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)
