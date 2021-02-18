# open a file for reading
f = open("pandp.txt", "r", encoding="utf=8")

# for each line in the file, print it out preceded by
# "And Jane Austen said: ")
for line in f:
    print("And Jane Austen said: " + line)
f.close()

# same thing, but using with syntax so you don't
# need to close the file
with open("pandp.txt") as f:
    for line in f:
        print(line)


