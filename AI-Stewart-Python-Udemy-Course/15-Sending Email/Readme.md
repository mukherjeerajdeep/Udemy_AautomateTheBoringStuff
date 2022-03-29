Sending email 

```python
import smtplib, ssl

conn = smtplib.SMTP('smtp.gmail.com', 587)

context = ssl.create_default_context()
conn.starttls(context=context)
(220, b'2.0.0 Ready to start TLS')
conn.ehlo()
(250, b'smtp.gmail.com at your service, [31.182.204.51]\nSIZE 35882577\n8BITMIME\nAUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')

conn.login('bmthecoder@gmail.com', 'January@2008')
Traceback (most recent call last):
  File "<pyshell#428>", line 1, in <module>
    conn.login('bmthecoder@gmail.com', 'January@2008')
  File "C:\Python\lib\smtplib.py", line 750, in login
    raise last_exception
  File "C:\Python\lib\smtplib.py", line 739, in login
    (code, resp) = self.auth(
  File "C:\Python\lib\smtplib.py", line 662, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials d18-20020adff2d2000000b001f025ea3a20sm10559893wrp.0 - gsmtp')


conn = smtplib.SMTP('smtp.gmail.com', 587)
context = ssl.create_default_context()
conn.starttls(context=context)
(220, b'2.0.0 Ready to start TLS')
conn.ehlo()
(250, b'smtp.gmail.com at your service, [31.182.204.51]\nSIZE 35882577\n8BITMIME\nAUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')

conn.login('bmthecoder@gmail.com', 'qadtezlrlcnhtltl')
Traceback (most recent call last):
  File "<pyshell#436>", line 1, in <module>
    conn.login('bmthecoder@gmail.com', 'qadtezlrlcnhtltl')
  File "C:\Python\lib\smtplib.py", line 750, in login
    raise last_exception
  File "C:\Python\lib\smtplib.py", line 739, in login
    (code, resp) = self.auth(
  File "C:\Python\lib\smtplib.py", line 662, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials 7-20020a05600c228700b00389865c646dsm11799804wmf.14 - gsmtp')
```
Full Program 

```python
import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
(250, b'smtp.gmail.com at your service, [31.182.206.207]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')

smtp_object.starttls()
(220, b'2.0.0 Ready to start TLS')

email = getpass.getpass("Email: ")
password = getpass.getpass("Please password")
smtp_object.login(email,password)

from_address = getpass.getpass("Enter your email: ")
to_address = getpass.getpass("Enter the email of the recipient: ")
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address,to_address,msg)

smtp_object.quit()
```
