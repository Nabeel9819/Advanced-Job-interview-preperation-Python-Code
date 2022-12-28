from array import *

ab = array('I',[1,2,3,4,5,6,7,8])

newArray = array(ab.typecode, (a*2 for a in ab))

for e in newArray:
    print(e)
print(newArray)