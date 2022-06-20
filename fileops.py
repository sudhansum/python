
# fr = open("abc.txt",'r')
# # print(fr.read())
# print(fr.readline(),end ='#')
# print(fr.readline(4),end ='#')

f1=open('testpy.txt','r')
# f1.write("something")
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
# f1 = open("testpy.txt",'a')
# f1.write("writing a poem")
# print(f1.readable())
str = " "
while str:
    str = f1.readline()
    print(str,end='')
f1.close()