#tem que import o reduce
from functools import reduce

red = reduce(lambda x,y:x+y, [1,2,3,4,5])
print(red)

red = reduce(lambda x,y:x+y, ['1','2','3','4','5'])
print(red)
