n = int(input())

for i in range(n):
    arr = list(input())
    count = 0

    for w in arr:
        if w == ("("):
            count += 1

        else:
            count -= 1

        if count < 0:
           print("NO")
           break

    else:
        if count == 0:
            print("YES")
        else:
            print("NO")
