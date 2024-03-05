a,b,c,d = map(int, input())
ops = ["+","-"]

for op1 in ops:
    for op2 in ops:
        for op3 in ops:
            exp = '{}{}{}{}{}{}{}'.format(a,op1,b,op2,c,op3,d)
            if eval(exp) == 7:
                print('{}=7'.format(exp))
                exit()
