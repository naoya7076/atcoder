N = int(input())
mod = 10**9 +7
power = 1
for i in range(N):
    # 途中でそれぞれmodをとってもOK
    power = power * (i+1) % mod
print(power)
