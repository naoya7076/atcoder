# 2 <= N <= 10**5なのでfor-loopは1重まで
N = int(input())
a = []
for _ in range(N):
    a.append(int(input()))

position = 0
for step in range(N):
    if step == 0:
        position = a[position]
    else:
        position = a[position-1]
    if position == 2:
        print(step + 1)
        exit()
print(-1)
