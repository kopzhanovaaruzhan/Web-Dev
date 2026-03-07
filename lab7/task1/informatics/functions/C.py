def xor(x, y):
    return (not(x) and y) or (not(y) and x)

num=list(map(int, input().split()))
print(xor(*num))