def hansoo(n):
    if n < 100:
        return True
    
    num = str(n)
    return int(num[0]) - int(num[1]) == int(num[1]) - int(num[2])


n = int(input())
count = 0

for i in range(1, n + 1):
    if hansoo(i):
        count += 1

print(count)
