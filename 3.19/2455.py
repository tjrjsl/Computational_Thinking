off1, on1 = map(int, input().split())
off2, on2 = map(int, input().split())
off3, on3 = map(int, input().split())
off4, on4 = map(int, input().split())
s1 = s2 = s3 = s4 = 0

s1 = on1 - off1
s2 = s1 - off2 + on2
s3 = s2 - off3 + on3
s4 = s3 - off4 + on4

print(max(s1, s2, s3, s4))
