# Fun with list comprehensions, map, and for loops


# Here are two lists
a = [10, 11, 12, 13, 14]
b = [5, 4, 3, 2, 1]

# Task: Create a new list, c, that contains
# [5, 7, 9, 13]
# that is [10-5, 11-4, 12-3, 13-2, 14-1]

###############
## FOR LOOPS ##
###############

# one option
c1 = []
for i in range(len(a)):
    c1.append(a[i] - b[i])

# another option: create a function and apply that
def subtract(x, y):
    return x-y

c2 = []
for i in range(len(a)):
    c2.append(subtract(a[i], b[i]))

# third option: use zip
c3 = []
for i,j in zip(a,b):
    c3.append(i-j)
    # or c3.append(subtract(i,j))


#########################
## LIST COMPREHENSIONS ##
#########################

c4 = [i-j for i,j in zip(a,b)]

c5 = [subtract(i,j) for i,j in zip(a,b)]


####################
## MAP AND LAMBDA ##
####################

c6 = list(map(lambda i,j : i-j, a, b))

c7 = list(map(subtract, a, b))

c8 = list(map(lambda i,j : subtract(i,j), a, b))



print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)
print(c8)
