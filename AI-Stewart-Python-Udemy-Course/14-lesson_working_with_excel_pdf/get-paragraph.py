#! usr/bin/python3
#read the paragraphs from the doc file

import docx

def getText(fileName):
    doc = docx.Document(fileName)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('/AI-Stewart-Python-Udemy-Course/14-lesson_working_with_excel_pdf\\demo.docx'))
