m = int(input())        # 令第一個輸入為m
while True:             # 從第二個輸入到最後一個輸入(9999)
    n = int(input())    # 令輸入為n
    m = min(m, n)       # 比較m和n，m記下較小的
    if n == 9999:       # 如果讀到的是9999
        break           # 中斷無窮迴圈
print(m)                # 印出兩兩比較後，最終的最小值m