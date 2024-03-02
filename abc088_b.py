# AliceからN枚のカードを交互に取得する
# 互いが最大のカードを取得した場合のAliceはBobより何点多く取得できるか(Alice - Bob)
N = int(input())
a = list(map(int, input().split()))

Alice = 0
Bob = 0

a.sort(reverse=True)
for i, num in enumerate(a):
    if i % 2 == 0:
        Alice += num
    else:
        Bob += num
print(Alice - Bob)

