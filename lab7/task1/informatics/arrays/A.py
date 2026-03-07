num = int(input())
numbers = list(map(int, input().split()))

for i in range(0, num, 2):
    print(numbers[i], end=" ")