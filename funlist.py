l = [21, 25, 36, 8, 12, 4, 6, 16]


def even_odd(l):
    evenx = 0
    oddx = 0
    for i in l:
        if i % 2 == 0:
            evenx += 1
        else:
            oddx += 1
    return evenx, oddx


evenx, oddx = even_odd(l)
print("even number is {} and odd number is {}".format(evenx, oddx))
