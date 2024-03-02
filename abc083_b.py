N, A, B = map(int, input().split())

sum = 0
for num in range(N+1):
    digit_num_sum = 0
    arr_num = map(int, str(num)) # [2, 0]とか
    for digit_num in arr_num:
        int_digit = int(digit_num)
        digit_num_sum += int_digit
    if A <= digit_num_sum and digit_num_sum <= B:
        sum += num
print(sum)
