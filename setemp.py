
a = set()
print(a,"creates an empty set")

a1 = {1,2,3.4,"learning"}
print(a1)

str =set("Deepali")
print(str)
str.add(11)
print(str)
str.update([14])
print(str)
str.remove(14)
print(str)
str.discard('e')
print(str)
str.pop()
print(str)
str.clear()
print(str)
b = a1.copy()
print(b,"copy is  used to copy two sets")

f = {1,4,5,6,7}
s1 = frozenset(f)
print(s1)
f.add(22)
print(f)
print(s1,"frozen set does not update the set")
