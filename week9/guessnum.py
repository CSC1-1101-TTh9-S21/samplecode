# User picks number between 1 and 100.
# Computer tries to guess.


low = 1
high = 100
correct = "x" # any value that is not "C"

# while the users has not said it's correct
while correct != "C":

    # guess the midpoint of the possible range
    myguess = (high+low)//2
    print(low, high, myguess)

    # ask user if it's right
    correct = input("My guess is {}. Too H(igh), too L(ow), C(orrect)? ".format(myguess))

    # if user says "too high", lower high to 1 less than what computer guessed
    if correct == "H":
        high = myguess-1

    # otherwise, increase low to 1 more than what the computer guessed
    elif correct == "L":
        low = myguess + 1
	
