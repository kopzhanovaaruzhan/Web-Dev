import math

num=int(input())

for i in range(2, math.ceil(math.sqrt(num))):
    if(num%i==0):
        print(i)
        break
