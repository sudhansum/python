"""  FILTER MAP AND REDUCE USING LAMBDA """
# MAP FN IS USED TO APPLY SAME FUNCTION OVER A SEQUENCE map(a,b)
from functools import reduce

# def is_even(n):
#     return n%2==0


nums = [3, 2, 5, 6, 8, 1, 12]

evens = list(filter(lambda n: n % 2 == 0, nums))
double = list(map(lambda n: n * n, nums))
sum1 = reduce(lambda a, b: a + b, double)
print(evens)
print(double)
print(sum1)
print("filter fn filters the even numns from nums")





