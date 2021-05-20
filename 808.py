try:    # 試試
        # 切成三段
    ddd, dd, dddd = input().split('-')
        # 都轉整數
    int(ddd)
    int(dd)
    int(dddd)
        # 若還沒炸
    print('Valid SSN')
except: # 有炸的話
    print('Invalid SSN')