# 準備一個空的dict
# d = dict()
# 也可以這樣
d = {}

# 讓CJ得以input兩輪
for t in range(2):
    print(f'Create dict{t+1}:')
    while True:
        key = input('Key: ')
        if key == 'end':    # 讀到'end'結束建立字典
            break
        else:               # 否則字典d新增一對key:value
            d[key] = input('Value: ')

# sorted(d)是排序過的d的keys，不含values
keys = sorted(d)
for key in keys:
    print(f'{key}: {d[key]}')
