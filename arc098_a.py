N = int(input())
S = list(input())

west_sum = [0] * (N + 1)
east_sum = [0] * (N + 1)

for i in range(N):
    west_sum[i + 1] = west_sum[i] + (1 if S[i] == "W" else 0)
    east_sum[N - i - 1] = east_sum[N - i] + (1 if S[N - i - 1] == "E" else 0)

min_turn = float('inf')
for i in range(N):
    turn = west_sum[i] + east_sum[i + 1]
    min_turn = min(min_turn, turn)
print(min_turn)
