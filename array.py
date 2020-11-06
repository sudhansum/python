
from array import *


vals = array('i',[5,7,8,9])
print(vals.buffer_info()) #gives the size of the address
print(vals.typecode) #gives the type of integer
vals.reverse()  #to reverse the array
print(vals)# to print the reverse array

print(vals[0])# to print the values one by one

for i in range(4):
    print(vals[i])

for i in range(len(vals)): #if we do not know the length
    print(vals[i])

for e in vals:
    print(e)

sub = array('u',["a","e","i","o","u"])
print(sub)
newArray = array(vals.typecode,(a for a in vals))
print(newArray)

newArray = array(vals.typecode,(a*a for a in vals))
print(newArray)

