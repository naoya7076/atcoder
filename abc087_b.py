a = int(input())
b = int(input())
c = int(input())
x = int(input()) # Xは50の倍数

# 3重loopになりそう間に合うかな?
# -> loopを減らす方法が思い浮かばないので愚直に3重ループにした
number = 0
for five_hundred in range(a+1):
    for one_hundred in range(b+1):
        for fifty in range(c+1):
            sum = 500 * five_hundred + 100 * one_hundred + 50 * fifty
            if sum == x:
                number +=1
print(number)
