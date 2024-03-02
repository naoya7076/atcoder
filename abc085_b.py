# 何種類の異なる値があるのかを調べる
N = int(input())
d = []
for _ in range(N):
    d.append(int(input()))

kind = 0
variable_list = []
for num in d:
    if num not in variable_list:
        variable_list.append(num)
        kind += 1
print(kind)
