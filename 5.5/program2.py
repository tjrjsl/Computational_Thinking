import random

def def3(n):
    a = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(1, n * n * 10 - 1))
        a.append(row)
    return a

def def4(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            print("%5d" % a[i][j], end="")
        print()

n = int(input("N 입력: "))

if 1 < n <= 5:
    A = def3(n)

    changed = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(A[j][i])
        changed.append(row)

    print("original")
    def4(A)

    print("changed")
    def4(changed)

else:
    print("input error")
