#! python3

# mapIt.py:	launches a map in the browser
#			using a street address from
#			the command line or clipboard.

import webbrowser, sys
if len(sys.argv) > 1:
	# Get address from command line.
	address = ' '.join(sys.argv[1:])
else:
	# Get address from the clipboard
	address = pyperclip.paste()

webbrowser.open('https:/www.google.com/maps/place/' + address)