H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

# 結果を格納するH * Wの変数
ans = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            ans[i][j] = "#"
            continue
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                tmp_i, tmp_j = i+dy, j+dx
                if 0 <= tmp_i < H and 0 <= tmp_j < W:
                    if s[tmp_i][tmp_j] == "#":
                        count += 1
        ans[i][j] = count

for row in ans:
    print("".join(map(str,row)))

# H, W = map(int, input().split())
# s = [list(input()) for _ in range(H)]

# # 結果を格納するH * Wの変数
# prepare = [[0] * W for _ in range(H)]

# for i in range(H):
#     for j in range(W):
#         if s[i][j] == "#":
#             prepare[i][j] = "#"
#             continue
#         cnt = 0
#         for dx in range(-1, 2):
#             for dy in range(-1, 2):
#                 ni, nj = i + dx, j + dy
#                 if 0 <= ni < H and 0 <= nj < W:
#                     if s[ni][nj] == "#":
#                         cnt += 1
#         prepare[i][j] = str(cnt)
# print(prepare)
