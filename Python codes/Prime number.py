n = int(input("Enter a number to check Prime: "))

for i in range(2,9):
    a = i
    if n <= 9:
        if n % i == 0:
           break
        else:
            print("Prime")
            break
        
    if n % a == 0:
        print("not Prime")
        break
else:
    print("Prime")