# 右邊兩個輸入字串依序存入左邊兩個變數
x1, y1 = input(), input()
x2, y2 = input(), input()
# 先不轉浮點數以免輸入整數也印出小數點
print(f'( {x1} , {y1} )')
print(f'( {x2} , {y2} )')
# 此時字串轉浮點數才能算距離
x1, y1 = float(x1), float(y1)
x2, y2 = float(x2), float(y2)
# 二次方根 就是 二分之一次方
D = ( (x1-x2)**2 + (y1-y2)**2 ) ** 0.5
print(f'Distance = {D:.4f}')