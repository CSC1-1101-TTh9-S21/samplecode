name = "Harold"
year = 2023
major = "Chemistry"

# different ways to print out the same thing
print(name, "|||", year, "|||", major)
print(name + " ||| " + str(year) + " ||| " + major)
print(name, year, major, sep=" ||| ")
print("{} ||| {} ||| {}".format(name,year,major))
print(name, "|||", year, "|||", major, "\n", end="")


# different ways to write ou the same thing to a file

# open the file for writing (use the "w" argument!)
googoo = open("myout.txt", "w")

googoo.write(name + " ||| " + str(year) + " ||| " + major + "\n")
googoo.write("{} ||| {} ||| {}\n".format(name,year,major))

mystring = name + " ||| " + str(year) + " ||| " + major + "\n"
googoo.write(mystring)
myotherstring = "{} ||| {} ||| {}\n".format(name,year,major)
googoo.write(myotherstring)


# NOTE This line below won't work! Why?
# Because write() is not the same as print().
# write() can take only one argument: a string.
# print() can take multiple string arguments, plus things like sep and end.
# googoo.write(name, "|||", year, "|||", major)

# Don't forget to close your file!
googoo.close()

