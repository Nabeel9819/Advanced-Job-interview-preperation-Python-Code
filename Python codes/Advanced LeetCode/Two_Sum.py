a = [1,2,3,4,5,6,7,8,9,10]
tar = 10

b = {} #key : value

for i,n in enumerate(a):
    dif = tar - n
    if dif in b:
        print(b[dif],i)
    print(i , n)
    b[n] = i












