from collections import deque
# stackを用いた深さ優先探索
H,W = map(int, input().split())
c = [list(input()) for _ in range(H)]
seen = [[False] * W for _ in range(H)]

# sとgの座標を探す
stack = deque()
sx,sy,gx,gy = 0,0,0,0
for h in range(H):
    for w in range(W):
        if c[h][w] == "s":
            sx,sy = h,w
        if c[h][w] == "g":
            gx,gy = h,w
stack.append((sx,sy))
seen[sx][sy] = True

while stack:
    x,y = stack.pop()
    for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
        nx,ny = x+dx,y+dy
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if c[nx][ny] == "#":
            continue
        if seen[nx][ny]:
            continue
        stack.append((nx,ny))
        seen[nx][ny] = True

if seen[gx][gy]:
    print("Yes")
else:
    print("No")
