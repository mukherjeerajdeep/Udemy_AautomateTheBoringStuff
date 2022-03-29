Drawing and importing Image

```python
from PIL import Image
mac = Image.open('example.jpeg')
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    mac = Image.open('example.jpeg')
  File "C:\Python\lib\site-packages\PIL\Image.py", line 2953, in open
    fp = builtins.open(filename, "rb")
FileNotFoundError: [Errno 2] No such file or directory: 'example.jpeg'


import os
os.getcwd()
'C:\\Python'


os.path()
Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    os.path()
TypeError: 'module' object is not callable

cos.chdir("C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\23-Working-With-Images")
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    cos.chdir("C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\23-Working-With-Images")
NameError: name 'cos' is not defined. Did you mean: 'os'?

os.chdir("C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\23-Working-With-Images")

os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\23-Working-With-Images'


mac = Image.open('example.jpeg')
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    mac = Image.open('example.jpeg')
  File "C:\Python\lib\site-packages\PIL\Image.py", line 2953, in open
    fp = builtins.open(filename, "rb")
FileNotFoundError: [Errno 2] No such file or directory: 'example.jpeg'
mac = Image.open('example.jpg')

type(mac)
<class 'PIL.JpegImagePlugin.JpegImageFile'>

mac
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1993x1257 at 0x23022359120>


mac.show
<bound method Image.show of <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1993x1257 at 0x23022359120>>

mac.show()


# Cropping Image
mac.crop((0,0,100,100))
<PIL.Image.Image image mode=RGB size=100x100 at 0x23022067FD0>
mac.crop((0,0,100,100)).show
<bound method Image.show of <PIL.Image.Image image mode=RGB size=100x100 at 0x230223958A0>>
mac.crop((0,0,100,100)).show()

pencils = Image.open(pencils.jpg)
Traceback (most recent call last):
  File "<pyshell#290>", line 1, in <module>
    pencils = Image.open(pencils.jpg)
NameError: name 'pencils' is not defined

pencils = Image.open("pencils.jpg")
Traceback (most recent call last):
  File "<pyshell#292>", line 1, in <module>
    pencils = Image.open("pencils.jpg")
  File "C:\Python\lib\site-packages\PIL\Image.py", line 2953, in open
    fp = builtins.open(filename, "rb")
FileNotFoundError: [Errno 2] No such file or directory: 'pencils.jpg'

os.listdir()
['example.jpg', 'pencils.htm', 'Readme.md']


pencils = Image.open("pencils.jpg")

# check the image size
pencils.size
(1950, 1300)


# take 30% of the image
pencils.crop((0,0,1950/3,1300/3))
<PIL.Image.Image image mode=RGB size=650x433 at 0x230223958A0>

pencils.crop((0,0,1950/3,1300/3)).show()
```