This Chapter is for the regex tutorial

```python
import re

sample_text = 'I have a phone which has phone number'

# Now let's try with the normal search not using the pattern but a text instead
re.search('phone', sample_text)
OUTPUT
<re.Match object; span=(9, 14), match='phone'>

# This returns a match object and it is saying where the first 'phone' word was found inside the sentence. It will not say about the other phone word

# Now what to do with this returned matcher ?
matcher = re.search('phone', sample_text)

# Let's see what we have inside
matcher.start()
9
matcher.end()
14

matcher.group() # will return 'phone' itself, what we searched
'phone'

matcher.span() # we already see this will show the location of the word inside the sentence
(9, 14)

matcher.groups()
()

# Let's try to find all the words with 'phone' inside the sentence
matcher = re.findall('phone', sample_text) # will return a matcher again


re.findall('phone', sample_text) # will return a matcher again
OUTPUT
['phone', 'phone']

matches = re.findall('phone', sample_text) # will return the found object as list

matches
OUTPUT
['phone', 'phone']

# now if anyone want to iterate over the found words inside a sentence then they need to do it with finditer() method

for matches in re.finditer('phone', sample_text):
    print(matches)

OUTPUT    
<re.Match object; span=(9, 14), match='phone'>
<re.Match object; span=(25, 30), match='phone'>

# actual print of the words throughout the iterator
for matches in re.finditer('phone', sample_text):
    print(matches.group())

OUTPUT   
phone
phone
```
**Identifiers**
Now that we know the special character designations, we can use them along with quantifiers to define how many we expect.

![Identifier](https://user-images.githubusercontent.com/43293317/159553980-02f0e909-6720-42c7-afd3-7e21f449a2d5.PNG)


```python
text = "My telephone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
phone.group()
'408-555-1234'
```
**Quantifier**

![Quatifier](https://user-images.githubusercontent.com/43293317/159554131-b677f45e-abe8-416d-9721-5f1901cdaef6.PNG)


The `?` says the group matches zero or one times.
The `*` says the group matches zero or more times.
The `+` says the group matches one or more times.
The `curly braces` can match a specific number of times.
The `curly braces` with two numbers matches a minimum and maximum number of times.

```python
re.search(r'\d{3}-\d{3}-\d{4}',text)
<_sre.SRE_Match object; span=(23, 35), match='408-555-1234'>
```

**Groups**
What if we wanted to do two tasks, find phone numbers, but also be able to quickly extract their area code (the first three digits). We can use groups for any general task that involves grouping together regular expressions (so that we can later break them down).
Using the phone number example, we can separate groups of regular expressions using parenthesis:

Groups are created in regex strings with parentheses.
The first set of parentheses is group 1, the second is 2, and so on.
Calling `group()` or `group(0)` returns the full matching string, `group(1)` returns group 1's matching string, and so on.
Use `\( and \)` to match literal parentheses in the regex string.
The `| pipe` can match one of many possible groups.

```python
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
# The entire result
results.group()
'408-555-1234'
# Can then also call by group position.
# remember groups were separated by parenthesis ()
# Something to note is that group ordering starts at 1. Passing in 0 returns everything
results.group(1)
'408'
results.group(2)
'555'
results.group(3)
'1234'
# We only had three groups of parenthesis
results.group(4)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-32-866de7a94a57> in <module>()
      1 # We only had three groups of parenthesis
----> 2 results.group(4)

IndexError: no such group
```

**Additional Regex Syntax**
Or operator `|`
Use the pipe operator to have an or statement. For example

```python
re.search(r"man|woman","This man was here.")
<_sre.SRE_Match object; span=(5, 8), match='man'>
re.search(r"man|woman","This woman was here.")
<_sre.SRE_Match object; span=(5, 10), match='woman'>
```

**The Wildcard Character**
Use a "wildcard" as a placement that will match any character placed there. You can 
use a simple period `.` for this. For example:

```python
re.findall(r".at","The cat in the hat sat here.")
['cat', 'hat', 'sat']
re.findall(r".at","The bat went splat")
['bat', 'lat']
```

Notice how we only matched the first 3 letters, that is because we need a `.` for each 
wildcard letter. Or use the `quantifiers` described above to set its own rules.

```python
re.findall(r"...at","The bat went splat")
['e bat', 'splat']
```
However, this still leads the problem to grabbing more beforehand. Really we only 
want words that end with `"at"`.

```python
# One or more non-whitespace that ends with 'at'
re.findall(r'\S+at',"The bat went splat")
['bat', 'splat']
```

**Starts with and Ends With**
We can use the `^` to signal starts with, and the $ to signal ends with:
_Note that this is for the entire string, not individual words!_

```python
# Ends with a number
re.findall(r'\d$','This ends with a number 2')
['2']

# Starts with a number
re.findall(r'^\d','1 is the loneliest number.')
['1']
```

**Exclusion**
To exclude characters, we can use the `^` symbol in conjunction with a set of brackets `[]`. 
Anything inside the brackets is excluded. For example:

```python
phrase = "there are 3 numbers 34 inside 5 this sentence."
re.findall(r'[^\d]',phrase)
['t',
 'h',
 'e',
 'r',
 'e',
 ' ',
 'a',
 'r',
 'e',
 ' ',
 ' ',
 'n',
 'u',
 'm',
 'b',
 'e',
 'r',
 's',
 ' ',
 ' ',
 'i',
 'n',
 's',
 'i',
 'd',
 'e',
 ' ',
 ' ',
 't',
 'h',
 'i',
 's',
 ' ',
 's',
 'e',
 'n',
 't',
 'e',
 'n',
 'c',
 'e',
 '.']
```

To get the words back together, use a `+` sign

```python
re.findall(r'[^\d]+',phrase)
['there are ', ' numbers ', ' inside ', ' this sentence.']
```

We can use this to remove punctuation from a sentence.

```python
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
re.findall('[^!.? ]+',test_phrase)
['This',
 'is',
 'a',
 'string',
 'But',
 'it',
 'has',
 'punctuation',
 'How',
 'can',
 'we',
 'remove',
 'it']
clean = ' '.join(re.findall('[^!.? ]+',test_phrase))
clean
'This is a string But it has punctuation How can we remove it'
```

**Brackets for Grouping**
As we showed above we can use brackets to group together options, for example if we 
wanted to find `hyphenated` words:

```python
text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
re.findall(r'[\w]+-[\w]+',text)
['hypen-words', 'long-ish']
```

**Parenthesis for Multiple Options**
If we have multiple options for matching, we can use `parenthesis` to list out these 
options. 
For Example:

```python
# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"
re.search(r'cat(fish|nap|claw)',text)
<_sre.SRE_Match object; span=(27, 34), match='catfish'>
re.search(r'cat(fish|nap|claw)',texttwo)
<_sre.SRE_Match object; span=(32, 38), match='catnap'>
# None returned
re.search(r'cat(fish|nap|claw)',textthree)
```

Leaving out the first or second number in the curly braces says there is no minimum or maximum.
"Greedy matching" matches the longest string possible, "**nongreedy matching**" (or "lazy matching") matches the shortest string possible.
Putting a question mark after the curly braces makes it do a **nongreedy/lazy** match.

**Unzipping and Zipping Files**

As you are probably aware, files can be compressed to a zip format. Often people use 
special programs on their computer to unzip these files, luckily for us, Python can do 
the same task with just a few simple lines of code.

**Create Files to Compress**
```python
# slashes may need to change for MacOS or Linux
f = open("new_file.txt",'w+')
f.write("Here is some text")
f.close()
# slashes may need to change for MacOS or Linux
f = open("new_file2.txt",'w+')
f.write("Here is some text")
f.close()
```

**Zipping Files**
The [zipfile library](https://docs.python.org/3/library/zipfile.html)is built in to Python, we can use it to compress 
folders or files. To compress all files in a folder, just use the `os.walk()` method to iterate this process
for all the files in a directory.

```python
import zipfile
Create Zip file first , then write to it (the write step compresses the files.)

comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()
```

**Extracting from Zip Files**
We can easily extract files with either the `extractall()` method to get all the files, or just using the `extract()` 
method to only grab individual files.

```python
zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")
```

**Using shutil library**
Often you don't want to extract or archive individual files from a `.zip`, but instead archive everything at once. 
The shutil library that is built in to python has easy to use commands for this:

The shutil library can accept a format parameter, format is the archive format: one of "`zip`", "`tar`", "`gztar`", 
"`bztar`", or "`xztar`".

```python
import shutil

pwd
'C:\\Users\\Marcial\\Pierian-Data-Courses\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules'
directory_to_zip='C:\\Users\\Marcial\\Pierian-Data-Courses\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules'
# Creating a zip archive
output_filename = 'example'
# Just fill in the output_filename and the directory to zip
# Note this won't run as is because the variable are undefined
shutil.make_archive(output_filename,'zip',directory_to_zip)
'C:\\Users\\Marcial\\Pierian-Data-Courses\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\example.zip'
# Extracting a zip archive
# Notice how the parameter/argument order is slightly different here
shutil.unpack_archive(output_filename,dir_for_extract_result,'zip')
```
