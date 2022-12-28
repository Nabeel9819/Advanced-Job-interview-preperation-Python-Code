i=1
j=1
while i <= 10:
    print(i," ", end="")
    j = i + 1
    while j <= 10:
        print(j," ",end="")
        j+=1
    i += 1
    print("\n")

x = "Nabeel"

for i in range(1,50):
    if i%5 == 0:
        print(i)