a=input()
b=a[::-1]

while b[0]=='0':
    b=b[1::]

print(b)