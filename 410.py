n = int(input())
for i in range(n, 0, -1): # i從n到1
    print(' '*(i-1) + '*'*(1+2*(n-i)))
    # 空白有i-1個 星星有1+2(n-i)個 字串相加接起來