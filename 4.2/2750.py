n = int(input())
arr =[]

for i in range(n):
    k = int(input())
    arr.append(k)
    
arr.sort()
for i in range(n):
    print(arr[i])
