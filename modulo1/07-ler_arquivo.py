file = open("arquivo.txt", "r")
doc = file.read()
# doc = file.readline()
# doc = file.readlines()
file.close()
print(doc)
print(type(doc))
