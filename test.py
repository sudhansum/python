

s = "hello"
for i in s:
    print(i*2,end=" ")
print()

s = input("enter the string:\n")
res = ""
for i in s:
    res = res+i*2
print("Output =",res, end=" ")