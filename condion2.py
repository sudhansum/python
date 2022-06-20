# while , while else , pass statement

i = 0
while (i < 2):
    print("hello")
    i = i + 1

n = int(input("enter your number"))
f = 1
while (i < n):
    f = f * i
    i += 1
print(f)

i=3
while(i<6):
    print(i)
    i=i+1
else:
    print("else")

n=5
m=1
while(m<=9):
    if(m==10):
        print("out of while liio")
        break
    print(m)
    m=m+1
else:
    print("no break statement,only else statement,only")

