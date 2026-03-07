import math
num=int(input())
i=2

while i<=math.sqrt(num):
    if(num%i==0):
        print(i)
        break
    i+=1