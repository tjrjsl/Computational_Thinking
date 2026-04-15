s = set()

def d(n):
    return n + sum(map(int, str(n)))

for i in range(1, 10001):
    a = d(i)
    if a <= 10000:
        s.add(a)

for i in range(1, 10001):
    if i not in s:
        print(i)
