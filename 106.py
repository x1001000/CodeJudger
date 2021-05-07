x = float(input())
y = float(input())
z = float(input())
S = (z/1.6) / ((x*60+y)/3600)   # 英哩除以小時
print(f'Speed = {S:.1f}')
# 若把第4行等號右邊算式直接取代第5行S，可以少一行