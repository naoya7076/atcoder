# 1秒後に上下左右のどちらかに1移動する。t秒後に(x,y)にいるかどうかを判定する
N = int(input())
t = [0] * (N+1)
x = [0] * (N+1)
y = [0] * (N+1)
t[0], x[0], y[0] = 0, 0, 0
for i in range(N):
    #上から順番に代入していく
    t[i+1], x[i+1], y[i+1] = map(int, input().split())
for i in range(N):
    dt = t[i+1] - t[i]
    dist = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])
    if dt < dist:
        print("No")
        exit()
    else:
        if dt % 2 != dist % 2:
            print("No")
            exit()
print("Yes")
