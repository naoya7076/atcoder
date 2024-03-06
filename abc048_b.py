a,b,x = map(int, input().split())

ans_b = b // x + 1
ans_a = (a-1) // x + 1

print(ans_b - ans_a)
