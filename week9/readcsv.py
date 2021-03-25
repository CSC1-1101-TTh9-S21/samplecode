# open csv file
f = open("pretendgrades.csv")

# read csv file into a list of lists
grades = []
labels = f.readline()
for line in f:

    # split on comma!
    parts = line.rstrip().split(",")

    # turn stuff into an int!
    grades.append([int(x) for x in parts[1:]])

f.close()
print(grades)

# one way to loop through print out the averages
for row in grades:
    print(sum(row)/len(row))

# another way to loop through print out the averages
for i in range(len(grades)):
    print(sum(grades[i])/len(grades[i]))

