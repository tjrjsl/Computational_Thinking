n = int(input())


for i in range(n):
    up = 0
    m = list(map(int, input().split()))
    num = m[0]
    score = m[1:]
    average = sum(score) / num
    
    for j in score:
        if j > average:
            up += 1
            
    per = up / num * 100
    print(f"{per:.3f}%")
