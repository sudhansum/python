from bs4 import BeautifulSoup
import requests
import pandas as pd

# data = BeautifulSoup(open("Demo.html"),'html.parser')
# print(type(data))
# print(data.find_all('title'))
# print(data.find_all('p'))

url = 'https://www.ndtv.com/coronavirus/india-covid-19-tracker'
html = requests.get(url)
data = BeautifulSoup(html.text, 'html.parser')
# print(data.find_all('table'))
t = data.find_all('table')
print(t)
r = t[0].find_all('tr')  # tr is table row
h = [i.text.strip() for i in r[0]]  # header of the row ie state cased..
# i.text is only for textual data strip is a fn to return string
print(h)
'''Extracting the data'''
''' states and its value'''
r = t[0].find_all('tr')  # r = rows , tr = table rows
x = []
for i in r:
    td = i.find_all('td')  # TABLE DATA(TD)
    y = [i.text for i in td]
    x.append(y)
x.pop(0)  # removes the 0th element
# print(x)
for i in x:
    i[0] = i[0][:i[0].find('DistrictCases')]
    print(i[0])
for i in x:
    i[1] = i[1][:i[1].find(' ')]
    i[2] = i[2][:i[2].find(' ')]
    i[3] = i[3][:i[3].find(' ')]
    i[4] = i[4][:i[4].find(' ')]

df = pd.DataFrame(x, columns=h)  # column as header
print(df)
