# まずは全探索
n = int(input())
a = list(map(int, input().split()))

divide_num = 0
while True:
    exists_odd = False
    for element in a:
        print(element)
        if element % 2 != 0:
            exists_odd = True
    if exists_odd:
        break
    for i, element in enumerate(a):
        a[i] = element / 2
    divide_num +=1
print(divide_num)
