N,K = map(int, input().split())
A = list(map(int, input().split()))

ans = -1
left = 0
right = N-1
while left <= right:
    middle = (right + left) // 2
    if K <= A[middle]:
        ans = middle
        right = middle - 1
    else:
        left = middle + 1
print(ans)
