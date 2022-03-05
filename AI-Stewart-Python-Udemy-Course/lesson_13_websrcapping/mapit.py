import pyperclip
import sys
import webbrowser

sys.argv  # ['mapit.py' , '870' , 'Valencia' , 'St'.]

# Check if command line argument were passed
if len(sys.argv) > 1:
    # Slice and join the rest of the list leaving the first index.
    address = ' '.join(sys.argv[1:])  # start from index 1 till end
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
