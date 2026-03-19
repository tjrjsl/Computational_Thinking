for i in range(3):
    a = list(map(int, input().split()))
    
    if a.count(1) == 3:
        print("A")
    elif a.count(1) == 2:
        print("B")
    elif a.count(1) == 1:
        print("C")
    elif a.count(1) == 0:
        print("D")
    else:
        print("E")
