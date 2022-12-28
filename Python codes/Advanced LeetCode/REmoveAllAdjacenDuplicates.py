'''
s='acabbca'
ans = []
for c in s:
    if ans and ans[-1] == c: 
        ans.pop()
    else: ans.append(c)
print(''.join(ans))


b ='Amaan'
list_1 = []
for a in b:
    print(list_1)
    #print(list_1[-1])
    if list_1[-1] == a:
        list_1.pop()
        print(list_1)
        print(list_1[-1])
    else:
        list_1.append(a)
        print(list_1)
        print(list_1[-1])
    
print(''.join(list_1))

'''
amaan = 'aaaasaaaa'

list1 = []
for a in amaan:
    if list1 !=[] and list1[-1] == a:
        list1.pop()
    else:
        list1.append(a)
print("Answer:","".join(list1))

#print(list1[-1])
#print("".join(list1))