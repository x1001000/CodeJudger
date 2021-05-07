# 當 A = BQ + R
# gcd(A,B) = gcd(B,R) = ...
# 輾轉相除下去可求得最大公因數
# 總之這題先背起來
def compute(x, y):
    if y == 0:
        return x
    else:
        return compute(y, x%y)

x, y = input().split(',')
x, y = int(x), int(y)
print(compute(x, y))