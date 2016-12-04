#! python3
#---------------------------------------
# mapIt.py - launches a map in the browser
# using an address form the command line
# or clipboard
#---------------------------------------
#
# execute in the command line:
#
#   python3 mapIt.py <location>
#
#---------------------------------------
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # get address from the command line
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)
