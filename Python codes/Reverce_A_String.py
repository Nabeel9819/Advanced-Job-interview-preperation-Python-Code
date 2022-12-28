a = "Amaan"
b = []
i = len(a)
i -=1
c = ""
print(i)
'''
#Type 1 
for z in reversed(range(len(a))):
    print(a[z])
    b.append(a[z])
print("".join(b))

    #b.append(c)
    #i-=i
#print(b)
'''
#Type 2
while i >= 0:
    print(a[i])
    b.append(a[i])
    i-=1
print(''.join(b))