word = "Donkey"

with open("file.txt", "r") as f:
    content = f.read()

content = content.replace(word, "######")

with open("file.txt", "w") as f:
    f.write(content)