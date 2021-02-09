# findhundreds.py

### To run this program, go to Run-> Run... Customized ###
### Then enter the integer you want to test in the box ###

# This is called importing a library.
# This library lets us read command line arguments.
import sys

# Here's how I get the first command line argument.
# You can memorize this syntax for now.
mynumber = int(sys.argv[1])

# Here's the how to get the hundreds place.
# Each // 10 chops off the last digit.
# At the end % 10 returns whatever the last digit is.
hundreds = ((mynumber // 10) // 10) % 10

# Print out the user's input and the hundreds place.
print(mynumber, hundreds)  # I can write comments here, too!

