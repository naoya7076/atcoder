N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A = [A1, A2]
S = [[0] * N, [0] * N]
for i in range(2):
    for j in range(N):
        if i == 0:
            if j == 0:
                S[0][0] = A[0][0]
            else:
                S[0][j] = S[0][j-1] + A[0][j]
        else:
            # S[0][j]とS[1][j-1]を比較して、大きい方とA[]
            if j == 0:
                S[1][0] = A[1][0] + S[0][0]
            else:
                bigger = max(S[0][j], S[1][j-1])
                S[1][j] = A[1][j] + bigger
print(S[1][N-1])


