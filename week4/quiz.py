for q in range(85, 60, -5):
    print(q, end=" ")
print("\n")


for p in range(10, -1):
    print(p)

vowels = "AEIOU"
output = ""
for ch in "ALIGATOR":
    if ch not in vowels:
        output = ch + " " + output
print(output)

