a, b = map(int, input().split())
result = []

for i in range(1, b+1):
    c = a * i
    c = str(c)
    c = c[::-1]
    c = int(c)
    result.append(c)

print(max(result))
