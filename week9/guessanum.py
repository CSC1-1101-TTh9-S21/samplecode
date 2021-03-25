import random

# function that tries to guess the number
# that was passed in as an argument
# it returns the number of guesses required
def guessnum(n):
    high = 100
    low = 1
    theguess = (high+low)//2
    guesscount = 1
    while theguess != n:
        if theguess > n:
            high = theguess - 1
        else:
            low = theguess + 1
        theguess = (high+low)//2
        guesscount += 1
    return guesscount

# function that submits 1000 random numbers
# to guessnum() and keeps track of how long
# it too to guess it for each one
# Returns a list of all the guess counts
def simulate():
    allguesscounts = []
    for i in range(1000):
        thenum = random.randint(1,100)
        guessesrequired = guessnum(thenum)
        allguesscounts.append(guessesrequired)
    return allguesscounts
        
# main method that prints out average number of guesses
def main():
    print(guessnum(3))
    allguess = simulate()
    print(sum(allguess)/len(allguess))
    print(allguess)

main()
