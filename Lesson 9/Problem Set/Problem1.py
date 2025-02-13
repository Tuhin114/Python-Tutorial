f = open("poem.txt")
data = f.read()

if "twinkle" in data:
    print("Twinkle is present in the poem")
else:
    print("Twinkle is not present in the poem")

f.close()