# 準備一個空的dict
# d = dict()
# 也可以這樣
d = {}

while True:
    key = input('Key: ')
    if key == 'end':    # 讀到'end'結束建立字典
        break
    else:               # 否則字典d新增一對key:value
        d[key] = input('Value: ')

try:    # 查查看字典
    d[input('Search key: ')]
except: # 若是d沒有的key 程式本該炸掉 進例外處理
    print(False)
else:   # 若沒進例外處理 也就是d有那個key
    print(True)