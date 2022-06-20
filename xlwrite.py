import xlsxwriter as df
from xlsxwriter import Workbook


w = df.Workbook("C:\\Users\\SUDHANSU\\Desktop\\a.xlsx")
w1= w.add_worksheet("my")
print("creating a worksheet with name w1")
w1.write("A1","NAME")
w1.write("B1","ROLLNO")
w1.write("C1","ADDRESS")
b = ["deepali","abc","xyz"]
c = [12,13,14]
d = ["ad1","ad2","ad3"]
# w1.write("A2",b[0])
# w1.write("A3",b[1])
# w1.write("A4",b[2])
# w1.write("B2",c[0])
# w1.write("B3",c[1])
# w1.write("B3",c[2])
# w1.write("C2",d[0])
# w1.write("C3",d[1])
# w1.write("C3",d[2])
for i in range(1,len(b)+1):
    w1.write(i,0,b[i-1])
    w1.write(i,1,c[i-1])
    w1.write(i,2,c[i-1])

w1.write_formula("B6","=SUM(B2:B4)")
w.close()