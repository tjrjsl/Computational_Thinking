n = int(input())
card = list(map(int, input().split()))

count = {}

for i in card:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

m = int(input())
choice = list(map(int, input().split()))

for i in choice:
    if i in count:
        print(count[i], end=' ')
    else:
        print(0, end=' ')
