def commonchar(s1, s2):
    for c in s1:
        if c in s2:
            print(c, "is in both strings")


def commonchar2(s1, s2):
    for i in range(len(s1)):
        if s1[i] in s2:
            print(s1[i], "is in both strings")

def main():
    mystring1 = input("enter a string: ")
    mystring2 = input("enter another string: ")
    commonchar(mystring1, mystring2)
    commonchar2(mystring1, mystring2)


main()
