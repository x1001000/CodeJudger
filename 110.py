import math
n = int(input())
s = int(input())
# 把題目數學公式用Python語言照抄
A = (n*s**2)/(4*math.tan(math.pi/n))
print(f'Area = {A:.4f}')