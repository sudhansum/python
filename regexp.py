import re

str = 'ab12$yccc4567v#'
x = re.findall("[abc]", str)
print(x)

str2 = 'ab12$y4567v#'
x2 = re.findall('[a-z]', str)
print(x2)

str3 = 'ab12$y4567v#'
x3 = re.findall('[^abc]', str)
print(x3, "not abc as the carat^^ symbol is used")

str4 = 'ab12$y4567v#'
x4 = re.findall('[0-9abcA-Z]', str)
print(x4)

str5 = 'ab12$y4567v#'
x5 = re.findall('[0-9abcA-Z]', str)
print(x5, "looking /s,/t/n for white space characters")

str6 = 'ab12$y4567v#'
x6 = re.findall('[0-9abcA-Z+]', str6)
x7 = re.findall("[abc+]", str)
print(x6, "abc+,plus symbol is a quantifier ie how many times repeated")
print(x7, "abc*,star ie 0 or 1 time")
x8 = re.findall("[abc?]", str)
print(x8, "? checks for 1 occurrence")

email = 'abc@gmail.com,hg@yahoo.com,pqr.gmail'
x9 = re.findall('@\w+', email)
print(x9, " \w gives the alphanumeric char ")

strx = "tata steel is the biggest STEEL maker apple,egg,universe"
x10 = re.findall(r'\b[aeoiuAEIOU\w+]',strx)
print(x10, 'prints starting with a vowel')

strx1 = 'Anil DOB 12-04-2001,xyz DOB 11-01-2006,abc DOB 03-02-2014'
xstr = re.findall(r'\d{2}-\d{2}-\d{4}',strx1)
print(xstr,"prints the digits which repeats for n times ")



