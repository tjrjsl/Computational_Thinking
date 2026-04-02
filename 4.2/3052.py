arr = []

for i in range(10):
    n = int(input())
    r = n % 42
    if r not in arr:
        arr.append(r)
       
print(len(arr))
