H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

# loopが2重だがHとWはたかだが50なので間に合う
for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            for dy, dx in [(-1,0), (1,0),(0,-1),(0,1)]:
                ni, nj = i + dy, j + dx
                if 0 <= ni < H and 0 <= nj < W and s[ni][nj] == "#":
                    break
            else:
                print("No")
                exit()
print("Yes")
