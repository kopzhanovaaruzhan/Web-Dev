num = int(input())
numbers = list(map(int, input().split()))
cnt=False
for i in range(1, num):
    if(numbers[i]==numbers[i-1]):
        cnt=True

if cnt:
    print("YES")
else:
    print("NO")