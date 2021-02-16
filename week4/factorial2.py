def factorial1(n):
    facnum = 1
    for i in range(n):
        facnum *= (i+1)
    print(facnum)

def factorial2(n):
    facnum = 1
    for i in range(1, n+1):
        facnum *= i
    print(facnum)

def factorial3(n):
    facnum = 1
    for i in range(n, 0, -1):
        facnum *= i
    print(facnum)


def main():
    factorial1(6)
    factorial2(6)
    factorial3(6)

main()
