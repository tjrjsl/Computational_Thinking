n = int(input())
count = 0

first = n

while True:
    a = n // 10      
    b = n % 10       
    c = (a + b) % 10
    n = b * 10 + c
    count += 1

    if n == first:
        break

print(count)
