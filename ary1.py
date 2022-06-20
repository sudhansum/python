import numpy as np

x = np.array([[1,2],[3,4],[5,6]])
print(x)
y=np.append(x,[[8,9]],axis=0 )
print(y)
# y1=np.append(x,[[10],[11]],axis=1)
# print(x)

x1 = np.arange(1,11)
print(x1,"arange fn creates a sig-dim array")
x2 = np.insert(x1,1,999)
print(x2,"insert command is used to inset a value=999 at post1 ")

x2d = np.array([[1,2],[2,3]])
print(x2d)
y2d = np.insert(x2d,1,999,axis=0)
print(y2d,"the broadcasting will happen in row1")
yd = np.insert(x2d,1,[34,45],axis=0)
print(yd,"sufficient value at row1 so no broadcasting")
print("axis 0 will go column wise and axis =1 is row wise gives the max element")