# 輸入字串 轉浮點數
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
# f-string
# 大括號代變數
# 冒號設定格式
# >7.2f 靠右取7位 小數點後取2位
# <7.2f 靠左取7位 小數點後取2位
print(f'|{n1:>7.2f} {n2:>7.2f}|')
print(f'|{n3:>7.2f} {n4:>7.2f}|')
print(f'|{n1:<7.2f} {n2:<7.2f}|')
print(f'|{n3:<7.2f} {n4:<7.2f}|')