f = open("state_us.csv")

abbrev = {}
for line in f:
    parts = line.rstrip().split(",")
    abbrev[parts[1]] = parts[0]

f.close()

print(abbrev)
