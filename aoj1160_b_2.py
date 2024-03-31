import sys
sys.setrecursionlimit(10**7)

def dfx(x,y):
    field[h][w] = 0
    for dx,dy in [[1,0],[1,1],[0,1][-1,1],[-1,0],[-1,-1]]:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if field[nx][ny] == 0:
            continue
        dfs(nx,ny)
while True:
    W,H = map(int, input().split())
    if H == 0 or W == 0:
        break
    field = [list(map(int,input().split())) for _ in range(H)]

    count = 0
    for h in range(H):
        for w in range(W):
            if field[w][h] == 0:
                continue
            dfs(h,w)
            count += 1
    print(count)
