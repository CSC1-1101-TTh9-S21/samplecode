import numpy as np

# laborious code for reading in a csv file
grades = []
people= []
f= open("pretendgrades.csv")
labels = f.readline().rstrip().split(",")
for line in f:
    parts = line.rstrip().split(",")
    grades.append([int(p) for p in parts[1:]])
    people.append(parts[0])
f.close()

# convert list of list to numpy array!
print(grades)
npgrades = np.array(grades)
print(npgrades)

# print out mean of first row
print(np.mean(npgrades[0,:]))

# print out mean of first column
print(np.mean(npgrades[:,0]))

# print out averages of *each* row and *each* column
print(np.mean(npgrades, axis=0))
print(np.mean(npgrades, axis=1))

# Print out who got the highest grade on the first quiz
highestgrade = np.max(npgrades[:,0])
highestindex = np.argmax(npgrades[:,0])
print(highestgrade, highestindex)
print(people[highestindex], "got the highest grade", highestgrade)

# quicker way to do it!
print(people[np.argmax(npgrades[:,0])])
