n = int(input())

for i in range(n):
    ox = list(input())
    score = 0
    keep = 0
    
    for i in ox:
        if i == "O":
            keep += 1
            score += keep
        else:
            keep = 0
    
    print(score)
