# findthousands.py
# Emily Prud'hommeaux
# February 4, 2021

# Get a number from the user using input.
a = input("Enter a big integer: ")

# Get and print the thousands place using string indexing.
b = a[-4]
print(b)

# Get and print the thousands place using math operations.
c = (int(a) // 1000) % 10
print(c)
