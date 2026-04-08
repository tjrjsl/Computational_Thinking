import sys

k, l = map(int, sys.stdin.readline().split())
kmu = {}

for _ in range(l):
    num = sys.stdin.readline().strip()
    
    if num in kmu:
        del kmu[num]
    kmu[num] = 1

count = 0
for key in kmu:
    print(key)
    count += 1
    if count == k:
        break
