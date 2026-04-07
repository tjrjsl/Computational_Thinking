n = int(input())

book = {}

for i in range(n):
    name = input()

    if name in book:
        book[name] += 1
    else:
        book[name] = 1

top = 0
key = ""
for i in book:
    if book[i] > top:
        top = book[i]
        key = i
    elif book[i] == top:
        if i < key:
            key = i

print(key)
