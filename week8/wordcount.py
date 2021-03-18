f = open("mobydick.txt")
text = f.read().split()
f.close()

counts = {}
for w in text:
    counts[w] = counts.get(w,0) + 1

for k,v in counts.items():
    if v > 1000:
        print(k,v)

