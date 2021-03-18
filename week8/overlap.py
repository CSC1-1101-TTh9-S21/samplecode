string1 = "Four score and seven years ago our fathers\
            brought forth on this continent a new nation\
            conceived in liberty and dedicated to the proposition\
            that all men are created equal."

string2 = "Whose woods these are I think I know\
            his house is in the village though\
            he will not mind me stopping here\
            to watch his woods fill up with snow"

words1 = set()
for w in string1.split():
    words1.add(w)

for w in string2.split():
    if w in words1:
        print("Word overlap:", w)

