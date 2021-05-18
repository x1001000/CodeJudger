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

# d.items()是列出(key,value)的list，用key排序後，一一輪詢
for key, value in sorted(d.items()):
    print(f'{key}: {value}')