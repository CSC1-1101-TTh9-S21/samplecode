
# create your dictionary
wordlist = {}

# turn every word into a sorted, uniqued string of characters
# then have that as the key for a value that is a list of
# all words with that sorted, uniqued string of characters
def buildanagramlist():
    f = open("cmudict-utf8.txt")

    for line in f:
        parts = line.rstrip().split()
        word = parts[0]

        # if the word is longer than 3 and is all letters
        if len(word) > 3 and word.isalpha():

            # get the set of letters and then turn it into a list again
            letters = list(set(word))

            # sort that list of letters
            letters.sort()

            # turn that into a string, and make it the key
            mykey = "".join(letters)

            # add the current word to the list of possible
            # words for that key
            if mykey in wordlist:
                wordlist[mykey].append(word)
            else:
                wordlist[mykey] = [word]
            

    f.close()


# turn your intput word into a sorted, uniqued string of characters
# look it up and print out all the anagrams
def findanagram(s):
    letters = list(set(s))
    letters.sort()
    mykey = "".join(letters)
    print(mykey)
    if mykey.upper() in wordlist:
        print(wordlist[mykey.upper()])
    else:
        print("No anagrams!")



def main():
    buildanagramlist()
    findanagram("smell")

main()
                 
