# write a program to remove the char of odd index value in a string

#given string is 0123456789
#output = 02468

s ="0123456789"
res = " "
for i in range(len(s)):
    if i%2!= 0:
        continue
    res= res + s[ i ]
print("output ", res , end = '  ')