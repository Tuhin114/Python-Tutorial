f = open("file.txt")
print(f.read())
f.close()

# Same can be like this - 
with open("file.txt") as f:
    print(f.read())

# You don't need to close the file when you use with open() as f: because it automatically closes the file when you are done with it.