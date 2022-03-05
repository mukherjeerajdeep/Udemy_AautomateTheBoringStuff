
The OpenPyXL third-party module handles Excel spreadsheets (.xlsx files).
openpyxl.load_workbook(filename) returns a Workbook object.
get_sheet_names() and get_sheet_by_name() help get Worksheet objects.
The square brackets in sheet[‘A1'] get Cell objects.
Cell objects have a "value" member variable with the content of that cell.
The cell() method also returns a Cell object from a sheet.

```python
import openpyxl

import os
os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_13_websrcapping'


os.chdir('C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_14_working_with_excel_pdf')

os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_14_working_with_excel_pdf'

workbook = openpyxl.load_workbook('test.xlsx')

type(workbook)
<class 'openpyxl.workbook.workbook.Workbook'>

sheet = workbook.get_sheet_by_name('sheet1')

Warning (from warnings module):
  File "<pyshell#94>", line 1
DeprecationWarning: Call to deprecated function get_sheet_by_name (Use wb[sheetname]).
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    sheet = workbook.get_sheet_by_name('sheet1')
  File "C:\Python\lib\site-packages\openpyxl\compat\__init__.py", line 38, in new_func1
    return func1(*args, **kwargs)
  File "C:\Python\lib\site-packages\openpyxl\workbook\workbook.py", line 262, in get_sheet_by_name
    return self[name]
  File "C:\Python\lib\site-packages\openpyxl\workbook\workbook.py", line 288, in __getitem__
    raise KeyError("Worksheet {0} does not exist.".format(key))
KeyError: 'Worksheet sheet1 does not exist.'

sheet = workbook.get_sheet_by_name('Sheet1')

type(sheet)
<class 'openpyxl.worksheet.worksheet.Worksheet'>

# if we don't know the sheet names
sheets = workbook.get_sheet_names()

Warning (from warnings module):
  File "<pyshell#101>", line 1
DeprecationWarning: Call to deprecated function get_sheet_names (Use wb.sheetnames).

sheets
['Sheet1']

#get the contents from the cell of the sheet
sheet['A1']
<Cell 'Sheet1'.A1>

cellA = sheet['A1']

cellA.value()
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    cellA.value()
TypeError: 'str' object is not callable


cellA = sheet['A1']
cellA
<Cell 'Sheet1'.A1>

cellA.value()
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    cellA.value()
TypeError: 'str' object is not callable

type(cellA)
<class 'openpyxl.cell.cell.Cell'>

type(cellA.value())
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    type(cellA.value())
TypeError: 'str' object is not callable

cellA
<Cell 'Sheet1'.A1>
cellA.value()
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    cellA.value()
TypeError: 'str' object is not callable

cellA.value()
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    cellA.value()
TypeError: 'str' object is not callable

cellA.value
'Repo'

str(cellA.value)
'Repo'

str(sheet['C1'].value)
'Check prod num'


str(sheet['D2'].value)
'CAHxxxx'

str(sheet['D5'].value)
'CAHxxxx'

# with numbers
sheet.cell(row=1, column=1)
<Cell 'Sheet1'.A1>

# printing lot more cells

for i in range(1, 8):
    print(i, sheet.cell(row=i, column=1).value)

    
1 Repo
2 5g/sys
3 5g/src/ucl
4 None
5 5g/pp
6 5g/obs
7 None

# or to print all
for k in range(1, 8):
    for v in range(1, 8):
        print(k,v, sheet.cell(row=k, column=v).value)

        
1 1 Repo
1 2 Type
1 3 Check prod num
1 4 Product number
1 5 None
1 6 None
1 7 None
2 1 5g/sys
2 2 Source
2 3 CXS1040095/1
2 4 CAHxxxx
2 5 None
2 6 None
2 7 None
3 1 5g/src/ucl
3 2 Source
3 3 CAF101148
3 4 CAHxxxx
3 5 None
3 6 None
3 7 None
4 1 None
4 2 None
4 3 CAF101148/1
4 4 None
4 5 None
4 6 None
4 7 None
5 1 5g/pp
5 2 Source
5 3 CXS1040092/1
5 4 CAHxxxx
5 5 None
5 6 None
5 7 None
6 1 5g/obs
6 2 Source
6 3 CXS2010066/1
6 4 CAHxxxx
6 5 None
6 6 None
6 7 None
7 1 None
7 2 None
7 3 CXS2010070/1
7 4 None
7 5 None
7 6 None
7 7 None

```


You can view and modify a sheet's name with its "title" member variable.
Changing a cell's value is done using the square brackets, just like changing a value in a list or dictionary.
Changes you make to the workbook object can be saved with the save() method.

```python
# modify the excel workbook

wb = openpyxl.Workbook()

wb
<openpyxl.workbook.workbook.Workbook object at 0x0000023F018A5810>

wb.get_sheet_names
<bound method Workbook.get_sheet_names of <openpyxl.workbook.workbook.Workbook object at 0x0000023F018A5810>>

wb.get_sheet_names()
['Sheet']

sheet = wb.get_sheet_by_name('Sheet')
type(sheet)
<class 'openpyxl.worksheet.worksheet.Worksheet'>

sheet['A1'].value

sheet['A1'].value == None
True

sheet['A1'].value == 42
False

sheet['A1'].value = 42
sheet['A1'].value
42

os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_14_working_with_excel_pdf'

sheet['A2'].value = 'hello'

wb.save('Example.xlsx')

sheets = wb.get_sheet_names()
sheets
['Sheet']

wb.create_sheet
<bound method Workbook.create_sheet of <openpyxl.workbook.workbook.Workbook object at 0x0000023F018A5810>>
wb.create_sheet()
<Worksheet "Sheet1">

wb.save('Example.xlsx')
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    wb.save('Example.xlsx')
  File "C:\Python\lib\site-packages\openpyxl\workbook\workbook.py", line 407, in save
    save_workbook(self, filename)
  File "C:\Python\lib\site-packages\openpyxl\writer\excel.py", line 291, in save_workbook
    archive = ZipFile(filename, 'w', ZIP_DEFLATED, allowZip64=True)
  File "C:\Python\lib\zipfile.py", line 1240, in __init__
    self.fp = io.open(file, filemode)
PermissionError: [Errno 13] Permission denied: 'Example.xlsx'

wb.get_sheet_names()
['Sheet', 'Sheet1']

sheet2 = wb.create_sheet()
wb.get_sheet_names()
['Sheet', 'Sheet1', 'Sheet2']

Sheet2.title
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    Sheet2.title
NameError: name 'Sheet2' is not defined. Did you mean: 'sheet2'?

sheet2.title
'Sheet2'

sheet1.title
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    sheet1.title
NameError: name 'sheet1' is not defined. Did you mean: 'sheet'?

sheet1 = wb.get_sheet_names()[1]

sheet1.title
<built-in method title of str object at 0x0000023F00983DF0>

str(sheet1.title)
'<built-in method title of str object at 0x0000023F00983DF0>'

sheet2.title
'Sheet2'
sheet2.title = 'My new sheet'

wb.save()
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    wb.save()
TypeError: Workbook.save() missing 1 required positional argument: 'filename'
wb.save('Example2.xlsx')

wb.create_sheet(index=0, title='My Other Sheet')
<Worksheet "My Other Sheet">

wb.save('Example3.xlsx')
```

The **PyPDF2** module can read and write PDFs.
Opening a PDF is done by calling open() and passing the file object to PPdfFileReader().
A Page object can be obtained from the PDF object with the getPage() method.
The text from a Page object is obtained with the extractText() method, which can be imperfect.
New PDFs can be made from PdfFileWriter().
New pages can be appended to a writer object with the addPage() method.
Call the write() method to save its changes.

```python
import PyPDF2


os.getswd()
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    os.getswd()
AttributeError: module 'os' has no attribute 'getswd'. Did you mean: 'getcwd'?
import os

os.getcwd()
'C:\\Rajdeep_Mukherjee\\Udemy_AautomateTheBoringStuff\\AI-Stewart-Python-Udemy-Course\\lesson_14_working_with_excel_pdf'



pdfFile = open('meetingminutes1.pdf')

type(pdfFile)
<class '_io.TextIOWrapper'>

 pdfFile = open('meetingminutes1.pdf', 'rb')
 
SyntaxError: unexpected indent
pdfFile = open('meetingminutes1.pdf', 'rb')

type(pdfFile)
<class '_io.BufferedReader'>


reader = PyPDF2.PdfFileReader(pdfFile)
type(reader)
<class 'PyPDF2.pdf.PdfFileReader'>

reader.numPages
19

reader.getPage
<bound method PdfFileReader.getPage of <PyPDF2.pdf.PdfFileReader object at 0x0000023F0190C6A0>>
reader.getPage(0)
{'/Contents': [IndirectObject(961, 0), IndirectObject(962, 0), IndirectObject(963, 0), IndirectObject(964, 0), IndirectObject(965, 0), IndirectObject(966, 0), IndirectObject(967, 0), IndirectObject(968, 0)], '/CropBox': [0, 0, 612, 792], '/MediaBox': [0, 0, 612, 792], '/Parent': IndirectObject(953, 0), '/Resources': {'/ColorSpace': {'/CS0': IndirectObject(975, 0), '/CS1': IndirectObject(976, 0), '/CS2': IndirectObject(976, 0)}, '/ExtGState': {'/GS0': IndirectObject(977, 0)}, '/Font': {'/TT0': IndirectObject(979, 0), '/TT1': IndirectObject(981, 0), '/TT2': IndirectObject(983, 0), '/TT3': IndirectObject(985, 0), '/TT4': IndirectObject(987, 0), '/TT5': IndirectObject(989, 0)}, '/XObject': {'/Im0': IndirectObject(973, 0)}}, '/Rotate': 0, '/StructParents': 0, '/Type': '/Page'}

page = reader.getPage(0)

page.extractText()
'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of \nMarch 7\n, 2014\n        \n     The Board of Elementary and Secondary Education shall provide leadership and \ncreate policies for education that expand opportunities for children, empower \nfamilies and communities, and advance Louisiana in an increasingly \ncompetitive glob\nal market.\n BOARD \n of ELEMENTARY\n and \n SECONDARY\n EDUCATION\n  '

# for all the pages to read


for pagenum in range(reader.numPages):
    print(reader.getPage(pegenum).extractText())

    
Traceback (most recent call last):
  File "<pyshell#271>", line 2, in <module>
    print(reader.getPage(pegenum).extractText())
NameError: name 'pegenum' is not defined. Did you mean: 'pagenum'?
for pagenum in range(reader.numPages):
    print(reader.getPage(pagenum).extractText())

    
OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of 
March 7
, 2014
        
     The Board of Elementary and Secondary Education shall provide leadership and 
create policies for education that expand opportunities for children, empower 
families and communities, and advance Louisiana in an increasingly 
competitive glob
al market.
 BOARD 
 of ELEMENTARY
 and 
 SECONDARY
 EDUCATION
  
 LOUISIANA STATE BOARD OF ELEMENTARY AND SECONDARY EDUCATION
   MARCH 7, 2014
  
 The Louisiana Purchase Room
  Baton Rouge, LA
   
 
 
The Louisiana State Board of Elementary and Secondary Education met in 
regular
 session on
 March 7, 2014
, in the Louisiana Purcha
se Room, located in the Claiborne 
Building in Baton Rouge, Louisiana.  The meeting was called to order at 
9:17 a.m.
 by 
Board President 
Chas Roemer
 and opened with a prayer by
 Ms. Terry Johnson, Bossier 
Parish School System
.  
Board members present were 
Dr. Lottie Beebe, Ms. Holly Boffy, Mr. Jim Garvey, Mr.
 Jay 
Guillot, Ms.
 Carolyn Hill, Mr. Walter Lee, 
Dr. Judith Miranti, 
Mr. Chas Roemer
, and 
Ms. Jane Smith
.  Ms. Connie Bradford
 and Ms. Kira Orange Jones were
 absent.
  
Dr. Charlie Michel, Lafourche Parish Sch
ool System,
 led the Pledge of Allegiance.
  Agenda
 Item 2.
 On motion of Mr. Garvey, seconded by Ms. Boffy, the Board approved the 
agenda, as printed and disseminated.
 (Schedule 1)
  Agenda
 Item 3.
 On motion of Ms. Smith, seconded by Ms. Boffy, the Board app
roved the 
minutes of January 15, 2014.
  Agenda
 Item 4.
 Report by the State Superintendent of Education
  State Superintendent of Education John White provided an update on the 
intense and increased support that the LDE is providing to teachers to 
assist wi
th 
new academic expectations.  The LDE has established the 
following support structures:  
(1) 
network teams are working directly with 
superintendents; 
(2) 
district planning teams and district planning guides 
have been established in every district; and 
(3) teacher leader team
s are
 doubling to 4,000 next year.  Sample test items are being released.  The 
curriculum package for next year is being released.
  Next year™s 
assessment guides will be produced in the following weeks.
  
# Combine PDf1 and Pdf2

import PyPDF2

pdf1 = open('meetingminutes1.pdf', 'rb')
pdf2 = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdf1)
reader2 = PyPDF2.PdfFileReader(pdf2)



#loop both and add in a new docuement

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

    
for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

    
outFile = open('combined.pdf', 'wb')
writer.write(outFile)

outFile.close()


pdf1.close()
pdf2.close()
```

The Python-Docx third-party module can read and write .docx Word files.
Open a Word file with docx.Document()
Access one of the Paragraph objects from the "paragraphs" member variable, which is a list of Paragraph objects.
Paragraph objects have a "text" member variable containing the text as a string value.
Paragraphs are composed of "runs".  The "runs" member variable of a Paragraph object contains a list of Run objects.
Run objects also have a "text" member variable.
Run objects have a "bold", "italic", and "underline" member variables which can be set to True or False.
Paragraph and run objects have a "style" member variable that can be set to one of Word's built-in styles.
Word files can be created by calling add_paragraph() and add_run() to append text content.

```python
import docx

doc.Document('demo.docx')
Traceback (most recent call last):
  File "<pyshell#328>", line 1, in <module>
    doc.Document('demo.docx')
NameError: name 'doc' is not defined. Did you mean: 'docx'?

docx.Document('demo.docx')
<docx.document.Document object at 0x0000023F01BB0D40>

d =  docx.Document('demo.docx')

d.paragraphs
[<docx.text.paragraph.Paragraph object at 0x0000023F01D9ABC0>, <docx.text.paragraph.Paragraph object at 0x0000023F01D9AAD0>, <docx.text.paragraph.Paragraph object at 0x0000023F01D9AC80>, <docx.text.paragraph.Paragraph object at 0x0000023F01D9AB60>, <docx.text.paragraph.Paragraph object at 0x0000023F01D9AE90>, <docx.text.paragraph.Paragraph object at 0x0000023F01D9AD70>, <docx.text.paragraph.Paragraph object at 0x0000023F01D9AE30>]

d.paragraphs[0].text
'Document Title'

d.paragraphs[1].text
'A plain paragraph having some bold and some italic.'

p = d.paragraphs[1]
p.runs
[<docx.text.run.Run object at 0x0000023F01D9AC50>, <docx.text.run.Run object at 0x0000023F01D9AB90>, <docx.text.run.Run object at 0x0000023F01D9AC20>, <docx.text.run.Run object at 0x0000023F01D9AE30>]

# Check above there are 4 runs because of each changes in the text type.

p.runs[0].text
'A plain paragraph having some '

p.runs[3].text
'italic.'

p.runs[3].text = 'It is underlines and bold'
p.runs[3].bold = True
p.runs[3].underline = True

# save the doc
d.save('demo2.docx')

# change the styles

p.style = 'Title'
d.save('demo3.docx')

# create new docuement
d = docx.Document()

d.add_heading('My name')
<docx.text.paragraph.Paragraph object at 0x0000023F01D9B3A0>

d.add_paragraph('whats up')
<docx.text.paragraph.Paragraph object at 0x0000023F01D9B250>

d.save('demo4.docx')
```