

def person(name,**data): # ** is used to accept multiple arguments
    print(name)
    print(data)

    for i,j in data.items(): # we can also print using the key word arguments using the keyword=i and the variable=j
        print(i,j)
    

person(name= "users",age=32,city = "phonebook",mob = 987564123)