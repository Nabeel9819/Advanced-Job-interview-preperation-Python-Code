from ast import Break, Pass
from http.client import CONTINUE


x = "Nabeel"

for i in range(0,50,5):
    if i >= 35:
        continue
        print("End")
    else:
        if i%5 == 0:
            print("Answer",i)