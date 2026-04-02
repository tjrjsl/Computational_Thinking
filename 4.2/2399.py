n = int(input())
arr = list(map(int, input().split()))
result = 0
arr.sort()
pre = 0

for i in range(n):
        result += arr[i] * i - pre
        pre += arr[i]

print(result*2)
