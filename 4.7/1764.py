n, m = map(int, input().split())

listen = set()
see = set()

for i in range(n):
    listen.add(input())

for i in range(m):
    see.add(input())

listensee = sorted(listen & see)

print(len(listensee))

for i in listensee:
    print(i)
