#Q29. Reduce examples(product) from function import reduce
# print(reduce(lambda a,b: a*b,[1,2,3,4]))? 

from functools import reduce
print(reduce(lambda a,b:a*b,[1,2,3,4]))