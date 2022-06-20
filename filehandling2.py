
with open("python.txt","w+") as fr:
    fr.write("writing to python.txt")

fr = open("python.txt")
print('hello',file=fr)
print(f1.read())

