import pyperclip
import webbrowser
import sys

if len(sys.argv) == 1:
    webbrowser.open('https://www.google.com/maps/search/' + pyperclip.paste())
else:
    webbrowser.open('https://www.google.com/maps/search/' + " ".join(str(x) for x in sys.argv[1:]))
