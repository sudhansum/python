import csv
import matplotlib.pyplot as plt
import pandas as pd
import sys

# f = open("MyData.txt","r")
# print(f.readline(),end="#")
# print(f.readline(),end="#")
# print(f.readline(4),end='')
# f.write("adding after the popem",'w+')

#
# f1 = open("abc.txt","a")
# f1.write("testing new file")
# f1.write("Laptop")

f = open("abc.txt")
print(f.mode)
# f.close()
print(f.read())
print(f.readable())
print(f.writable())
print(f)
# 
# print("modes of a file")


# with open("company_sales_data.csv", "r") as fr:
#     data = csv.reader(fr)
#     # next(data)
#     # print("next will remove the heading")
#     header = []
#     header = next(data)
#     print(type(data))
#     print(header)
#     # for i in data:
#     #     print(i)
#
#     row = []
#     for row in data:
#         row.append(row)
#     print(row)
import runs as runs
#
# rows = []
# # facecream = []
# with open("company_sales_data.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row[0])
# print(header)
# print(rows)
# # c=["y",'green','red']
# plt.pie(rows,labels=rows)
# plt.show()
# print(facecream)


# fr = pd.read_csv("company_sales_data.csv")
# print(fr.head())
# print(fr.columns)
# # print(fr(["month_number "," facecream "]))
# print(fr.iloc[5])
