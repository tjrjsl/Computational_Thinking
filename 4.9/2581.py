import math

def prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True


m = int(input())
n = int(input())

plus = 0
mini = 0

for i in range(m, n + 1):
    if prime(i):
        plus += i
        if mini == 0:
            mini = i

if plus == 0:
    print(-1)
else:
    print(plus)
    print(mini)
