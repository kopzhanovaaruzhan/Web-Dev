num = int(input())
numbers = list(map(int, input().split()))
cnt=0
for i in range(num//2):
    numbers[num-i-1], numbers[i] = numbers[i], numbers[num-i-1]

for i in numbers:
    print(i, end=" ")