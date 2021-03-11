def updatestring(s1):
    s1 = s1 + "!!!"
    print(s1)

def updatestring2(s1):
    s1 = "hey there"
    print(s1)


def main():

    # mystring does not change after you
    # pass it in as an argument to the function 
    mystring = "foo"
    print("Here is the string: " + mystring)
    updatestring(mystring)
    print("Here is the string after calling updatestring(): " + mystring)
    updatestring2(mystring)
    print("Here is the string after calling updatestring2(): " + mystring)

main()
