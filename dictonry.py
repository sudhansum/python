# dictonary is mutable

dictn = {}
print(dictn, "empty dictionary is created")

d = {1: 'deepali', 2: 'mylearning', 3: 8}
print(d)

d1 = {'deepali': 20, "youtube": 30}
print(d1)

d2 = {1: [1, 2, 4], 4: 'hello'}
print(d2)

d3 = dict({'a': 1, 'b': 2})
print(d3, 'using dict keyword in the inside curley braces')

d4 = dict({1: 'deep', 4: 60})
print(d4, 'using dict key word')

d5 = {1: 'hello', 2: 60, 3: {5: 'python', 6: 70}}
print(d5, 'using nested dictionary')

print("adding element to dictionary")
d5[4] = 'hey'
print(d5, "added a new values and postn as 4 key value")
d5[3] = 70
print()
print(d5, "assigning the value at postn 3")
print()
d5["string"] = 32
print(d5, "changing the value")
print()
print(d5[4], "accessing the value at postn")
print(d5.get(3), "accessing the value using key fn")
print()
d5 = {1: 'hello', 2: 60, 3: {5: 'python', 6: 70}}
print(d5[3][6], "accessing the ualue from nested dictionary")
del d5[1]
print(d5, "deleting the key and value using fn")
d5.pop(2)
d5.popitem()
print(d5, "removes the last item")
d5.clear()
print(d5, "cleares the dictonary")
d6 = d.copy()
print(d6, "copies a dictonary")
print(d6.keys(), "gives the keys of the dict")
print(d6.items(), "gives the items in the dictionary")
