# この場合の解法。引数の与えられ方はatcoderの典型を参照
# https://qiita.com/uniTM/items/2f2a38f225f04154df9a
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_a

N,K = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = N-1
while left <= right:
    middle = (right + left) // 2
    if K == A[middle]:
        print(middle)
        exit()
    elif K < A[middle]:
        right = middle - 1
    elif K > A[middle]:
        left = middle + 1
print(-1)
