marks = {
    "Ravi" : 10,
    "Raj" : 20,
    "Rohit" : 30,
    0 : 40
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

marks.update({"Ravi" : 50, "Tuhin" : 100})
# print(marks)

# print(marks.pop("Ravi")) # returns removed value

# print(marks.popitem())

# print(marks)

print(marks.get("Ravi"))    # returns value
print(marks.get("Tuhin2"))   # returns None
print(marks["Tuhin2"])   # returns error