num = int(input())
numbers = list(map(int, input().split()))
cnt=0
for i in range(1, num):
    if(numbers[i]>numbers[i-1]):
        cnt+=1

print(cnt)