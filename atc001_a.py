# スタックオーバーフロー回避のため再帰深度上限を大きな値に設定
# スタックによる実装を行うことが理想
import sys
sys.setrecursionlimit(10**7)  
# 深さ優先探索
H,W = map(int, input().split())
c = [list(input()) for _ in range(H)]
seen = [[False] * W for _ in range(H)]

def dfs(x,y):
    for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
        nx,ny = x+dx,y+dy
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if c[nx][ny] == "#":
            continue
        if seen[nx][ny]:
            continue
        seen[nx][ny] = True
        dfs(nx,ny)

# sとgの座標を探す
sx,sy,gx,gy = 0,0,0,0
for h in range(H):
    for w in range(W):
        if c[h][w] == "s":
            sx,sy = h,w
        if c[h][w] == "g":
            gx,gy = h,w
dfs(sx,sy)
if seen[gx][gy]:
    print("Yes")
else:
    print("No")
