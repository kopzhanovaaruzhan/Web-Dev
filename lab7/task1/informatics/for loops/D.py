a = int(input())
b = int(input())
num=0
print(str(a).count(str(b)))

while a>0:
    if a%10==b:
        num+=1
    a//=10

print(num)

