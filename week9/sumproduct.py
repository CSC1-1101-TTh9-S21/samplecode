# take two ints, return product and sum
def twoints(x,y):
    a = x+y
    b = x*y
    return b, a

    # Oneliner version!
    # return a*b, a+b

# take two ints, submit them to twoints()
# return True if product > sum, False otherwise
def bigger(x,y):
    c = twoints(x,y)
    if c[0] > c[1]:
        return True
    else:
        return False

##    alternative naming elements of returned tuple
##    a,b = twoints(x,y)
##    if a > b:
##        return True
##    else:
##        return False


# main
def main():
    int1 = 8
    int2 = -2
    answer = bigger(int1, in2)
    if answer == True:
        print("The sum of {} and {} is less than the product".format(8,-2))
    else:
        print("The sum of {} and {} is greater than the product".format(8,-2))

main()
        
