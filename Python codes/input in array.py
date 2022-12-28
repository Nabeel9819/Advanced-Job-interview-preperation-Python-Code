from Array import *

arr1 = array('i',[145,542,543,674,765,76,784])
n = int(input("Length of Array: "))

for i in range(n):
    print("Enter the number for ",i, "Index")
    x= int(input())
    arr1.append(x)
print(arr1)

var_1 = 0
#Search in arr1
search = int(input("Enter the number to search: "))
for e in arr1:
    if search == e:
        print("The index for your number is: ", var_1)
        break
    if e == n:
        print("The number is not in the array")
    var_1 += 1

#print(arr1.index(n))