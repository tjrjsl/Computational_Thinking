n = int(input())
s = set()

for i in range(n):
    name, come = input().split()
    if come == "enter":
        s.add(name)
    else:
        s.remove(name)

s = sorted(s, reverse = True)

for name in s:
    print(name)
