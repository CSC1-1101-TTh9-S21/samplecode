import sys

# expert data structures task:
# map letter counts to a set of words with that length

def makething():
    # open file
    f = open(sys.argv[1])

    # create empty dictionary
    mydictionary = {}

    # for each line in the file
    for line in f:

        # get the words
        words = line.rstrip().split()

        # for every word in the file
        for w in words:

            # get its length
            count = len(w)

            # if that count is in the dictionary...
            if count in mydictionary:

                # add the word to the set that is its varlue
                mydictionary[count].add(w)

            # otherwise, create a dictionary entry for it
            else:
                mydictionary[count] = {w} # <- that's a set with one element!
    return mydictionary
    
def main():
    thething = makething()
    for k,v in thething.items():
        print(k,v)

main()
    
