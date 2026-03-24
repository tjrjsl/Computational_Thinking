n = int(input())

for i in range(1, n+1):
    print("*" * i)

for i2 in range(n+1, 2*n):
    print("*" * (2*n - i2))
