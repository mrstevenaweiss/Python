#!/Users/mrweiss/Development/code/python-practice/ python3
# mapIt.py

import webbrowser, sys

print(sys.argv)
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

webbrowser.open('https://www.google.com/maps/place/' + address)
