# Have to import sys to get command line arguments.
import sys


# This function greets the user based on commandline arguments provided.
# The first parameter is a string, and the second is a number.
def greeting(name, age):
    print("Hello,", name, "!")
    print("You will be", (age+4), "in 2025.")

# Here is the main function definition.
# It gets the input from the command line arguments, then calls greeting().
def main():
    a = sys.argv[1]
    b = int(sys.argv[2])  # converting to int!
    greeting(a, b)

# Here's where I run the main() function.
main()

