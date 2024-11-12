with open("arquivo.txt", "r") as file:
    doc = file.read()
    # doc = file.readline()
    # doc = file.readlines()
print(doc)
print(type(doc))
