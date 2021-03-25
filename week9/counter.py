# Copy and paste a news story into a text file on your desktop.
# Your goal will be to create a dictionary that maps each word to the
# number of vowels it has, e.g., elephant -> 3.

# Write a function that opens the file (you can use sys.argv[1]),
# reads it in line by line, splits each line into words,
# then for each word, add it to a dictionary, making its value the
# number of vowels it has. Then return the dictionary.

# Write a main function that calls this function and the prints out the number of keys in the dictionary.

import sys

vowels = "aeiou"

def openFile():
    voweldict = {}  # empty dictionary

    # open file to count in
    file = open(sys.argv[1])

    # for each line...
    for line in file.readlines():

        # split line into words
        words = line.split()

        # for each word...
        for word in words:

            # if it's all letters
            if word.isalpha():
                counter = 0

                # for each letter in the word
                for c in word:

                    # if it's a vowel, increase its count by 1
                    if c in vowels:
                        counter += 1

                # enter word into dictionary
                voweldict[word] = counter

    file.close()

    # return the dictionary
    return voweldict

def main():
    dictionary = openFile()
    print(len(dictionary.keys()))
    print(dictionary)

main()
