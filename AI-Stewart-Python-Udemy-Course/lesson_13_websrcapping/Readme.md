WebScrapping

```doctest
The Requests module is a third-party module for downloading web pages and files.
requests.get() returns a Response object.
The raise_for_status() Response method will raise an exception if the download failed.
You can save a downloaded file to your hard drive with calls to the iter_content() method.
```

```python
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.status_code
200

res.text[:500]
'The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare\r\n\r\nThis eBook is for the use of anyone anywhere at no cost and with\r\nalmost no restrictions whatsoever.  You may copy it, give it away or\r\nre-use it under the terms of the Project Gutenberg License included\r\nwith this eBook or online at www.gutenberg.org/license\r\n\r\n\r\nTitle: Romeo and Juliet\r\n\r\nAuthor: William Shakespeare\r\n\r\nPosting Date: May 25, 2012 [EBook #1112]\r\nRelease Date: November, 1997  [Etext #1112]\r\n\r\nLanguage: Eng'


res = requests.get('https://automatetheboringstuff.com/files/rj.txt/dhahdah')

res.raise_for_status()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    res.raise_for_status()
  File "C:\Users\erajmuk\AppData\Roaming\Python\Python310\site-packages\requests\models.py", line 960, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://automatetheboringstuff.com/files/rj.txt/dhahdah

playFile = open('RomeoJuliet.txt', 'wb') # In binary form

for chunk in res.iter_content(10000): # iter_contents returns bytes
    playFile.write(chunk)

    
315
playFile.close()

import os
os.getcwd()
'C:\\Python'

os.chdir('C:\Rajdeep_Mukherjee\Udemy_AautomateTheBoringStuff\AI-Stewart-Python-Udemy-Course\lesson_13_websrcapping')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 20-23: truncated \UXXXXXXXX escape

os.chdir('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_13_websrcapping')


res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
playFile = open('RomeoJuliet.txt', 'wb') # In binary form

for chunk in res.iter_content(10000): # iter_contents returns bytes
    playFile.write(chunk)
    
SyntaxError: multiple statements found while compiling a single statement

playFile = open('RomeoJuliet.txt', 'wb')
for chunk in res.iter_content(10000):
    playFile = open('RomeoJuliet.txt', 'wb')

    

playFile.close()


C:\Rajdeep_Mukherjee\Udemy_AautomateTheBoringStuff\AI-Stewart-Python-Udemy-Course\lesson_13_websrcapping
KeyboardInterrupt


res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
playFile = open('RomeoJuliet.txt', 'wb')

for chunk in res.iter_content(10000):
    playFile.write(chunk)

    
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
10000
8978

playFile.close()



import bs4


import requests

res = requests.get('https://www.amazon.in/Apple-MacBook-Chip-13-inch-512GB/dp/B08N5YD6NF/?_encoding=UTF8&pd_rd_w=ujOwP&pf_rd_p=4be2c5cb-3bad-4623-b15f-d7e062e89225&pf_rd_r=Q8N43W7VESP30MG4P9VS&pd_rd_r=9b73052e-d78b-45d5-80d7-acfdc5ce23a4&pd_rd_wg=7ijln&ref_=pd_gw_ci_mcx_mr_hp_atf_m')

res.raise_for_status()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    res.raise_for_status()
  File "C:\Users\erajmuk\AppData\Roaming\Python\Python310\site-packages\requests\models.py", line 960, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 503 Server Error: Service Unavailable for url: https://www.amazon.in/Apple-MacBook-Chip-13-inch-512GB/dp/B08N5YD6NF/?_encoding=UTF8&pd_rd_w=ujOwP&pf_rd_p=4be2c5cb-3bad-4623-b15f-d7e062e89225&pf_rd_r=Q8N43W7VESP30MG4P9VS&pd_rd_r=9b73052e-d78b-45d5-80d7-acfdc5ce23a4&pd_rd_wg=7ijln&ref_=pd_gw_ci_mcx_mr_hp_atf_m



res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_1?keywords=automate+the+boring+stuff+with+python&qid=1646424126&sprefix=automate+the+%2Caps%2C340&sr=8-1')

res.raise_for_status()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    res.raise_for_status()
  File "C:\Users\erajmuk\AppData\Roaming\Python\Python310\site-packages\requests\models.py", line 960, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 503 Server Error: Service Unavailable for url: https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_1?keywords=automate+the+boring+stuff+with+python&qid=1646424126&sprefix=automate+the+%2Caps%2C340&sr=8-1

res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/')

res.raise_for_status()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    res.raise_for_status()
  File "C:\Users\erajmuk\AppData\Roaming\Python\Python310\site-packages\requests\models.py", line 960, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 503 Server Error: Service Unavailable for url: https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/

res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/')

res.raise_for_status()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    res.raise_for_status()
  File "C:\Users\erajmuk\AppData\Roaming\Python\Python310\site-packages\requests\models.py", line 960, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 503 Server Error: Service Unavailable for url: https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/
```

```doctest
To import selenium, you need to run: "from selenium import webdriver" (and not "import selenium").
To open the browser, run: browser = webdriver.Firefox()
To send the browser to a URL, run: browser.get(‘https://inventwithpython.com')
The browser.find_elements_by_css_selector() method will return a list of WebElement objects: elems = browser.find_elements_by_css_selector(‘img')
WebElement objects have a "text" variable that contains the element's HTML in a string: elems[0].text
The click() method will click on an element in the browser.
The send_keys() method will type into a specific element in the browser.
The submit() method will simulate clicking on the Submit button for a form.
The browser can also be controlled with these methods: back(), forward(), refresh(), quit().
```