f = open("file.txt")

lines = f.readlines()
print(lines, type(lines))

line1 = f.readline()
print(line1, type(line1))

f.close()