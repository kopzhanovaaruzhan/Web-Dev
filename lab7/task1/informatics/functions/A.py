def minim(num1, num2, num3, num4):
    return min(num1, num2, num3, num4)

num1, num2, num3, num4 = map(int, input().split())

print(minim(num1, num2, num3, num4))