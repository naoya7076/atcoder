# バケット法
N = int(input())
d = []
for _ in range(N):
    d.append(int(input()))

bucket = [0] * 100
for num in d:
    bucket[num-1] += 1 # 配列が0始まりなので-1している
kind = 0
for i in bucket:
    if i != 0:
        kind +=1
print(kind)
