# 考える必要があるのは以下の2パターン
# - A <= C < B
# - C <= A < D
A, B, C, D = map(int, input().split())

if A <= C < B:
    if B <= D:
        print(B-C)
        exit()
    elif D < B:
        print(D-C)
        exit()
elif C <= A < D:
    if D <= B:
        print(D-A)
        exit()
    elif B < D:
        print(B-A)
        exit()
print(0)
