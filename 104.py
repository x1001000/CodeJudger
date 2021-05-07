import math             # 匯入math函式庫
R = float(input())      # 讓judge輸入半徑
P = 2 * math.pi * R     # 圓周長 = 2πr
A = math.pi * R ** 2    # 圓面積 = πrr
print(f'Radius = {R:.2f}')
print(f'Perimeter = {P:.2f}')
print(f'Area = {A:.2f}')