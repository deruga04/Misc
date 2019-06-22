import pyperclip
import webbrowser
import sys

browser = '/usr/bin/google-chrome %s'

try:
    query = str(sys.argv[1:]).join('+')
    webbrowser.open('https://www.youtube.com/results?search_query=' + query)
except:
    print('Please enter a search query')
    print('Example: python3 youtube.py sanctuary joji')
