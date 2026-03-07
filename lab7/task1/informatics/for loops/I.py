import math

num=int(input())
deli=0

for i in range(1, num+1):
    if(num%i==0):
        deli+=1

print(deli)