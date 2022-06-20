import re

str = 'Tata manufactures steels and saves India'
x = input()
y = re.search(x,str)
print(y,"it gives the match object in the string")


if y:
    print("found")
else:
    print("not found")
