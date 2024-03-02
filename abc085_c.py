# Nはお札の枚数
# Y<= 2 * 10^7であり、ループ減らす問題の可能性が高い
# 10000円の枚数をA, 5000円の枚数をB, 1000円をN-A-Bとする
# 合計金額 = 10000*A + 5000 * B + 1000 * (N-A-B)
N, Y = map(int, input().split())

for A in range(N+1): # 配列の数値は0始まりなのでN+1している
    for B in range(N+1-A): # この時点でA枚使われていることは確定しているので、あらかじめ引く
        C = N-A-B
        sum = 10000 * A + 5000 * B + 1000 * C
        if sum == Y:
            print(A, B, C)
            exit()
print(-1,-1,-1)
