
def power(num1, num2):
    return num1**num2

num= list(map(int, input().split()))
print(power(*num))