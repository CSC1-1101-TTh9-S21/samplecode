## GET STRING LENGTH

def getlengthI1(s):
    mylen = 0
    for i in s:
        mylen += 1
    return mylen

def getlengthI2(s):
    mylen = 0
    while s != "":
        s = s[1:]
        mylen += 1
    return mylen
    
def getlengthR(s):
    if s == "":
        return 0
    return 1 + getlengthR(s[1:])


## CALCULATE FACTORIAL
def factorialI(n):
    tots = 1
    for i in range(n):
        tots *= i+1
    return tots

def factorialR(n):
    if n == 1:
        return 1
    return n * factorialR(n-1)


## REVERSE STRING
def reversestringI(s):
    news = ""
    while len(s) > 0:
        news = s[0] + news
        s = s[1:]
    return news

def reversestringR(s):
    if len(s) == 1:
        return s
    return reversestringR(s[1:]) + s[0]



def main():
    print(getlengthI1("elephant"))
    print(getlengthI2("elephant"))
    print(getlengthR("elephant"))

    print(factorialI(5))
    print(factorialR(5))

    print(reversestringI("elephant"))
    print(reversestringR("elephant"))

main()


