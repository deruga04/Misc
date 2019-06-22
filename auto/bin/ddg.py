import pyperclip
import webbrowser
import sys

if len(sys.argv) == 1:
    webbrowser.open('https://duckduckgo.com/?q=' + pyperclip.paste())
else:
    webbrowser.open('https://duckduckgo.com/?q=' + " ".join(str(x) for x in sys.argv[1:]))
