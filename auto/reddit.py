import pyperclip
import webbrowser
import sys

if len(sys.argv) == 2:
    webbrowser.open('https://reddit.com/r/' + sys.argv[1])
else:
    print('Too many arguments!')