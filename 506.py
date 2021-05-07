def compute(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:       # 判別式>0，有兩解
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        return f'{x1}, {x2}'
    elif D == 0:    # 判別式=0，有一解
        x = -b / (2*a)
        return x
    else:   # 判別式<0，無解
        return 'Your equation has no root.'

# 寫成一行太長，故分成四行
a = int(input())
b = int(input())
c = int(input())
print(compute(a, b, c))
# 完整的寫法是
# print(compute(a=a, b=b, c=c))
# 等號右邊是全域變數，存入等號左邊的函數內區域變數
# 全域變數的a,b,c並非區域變數的a,b,c