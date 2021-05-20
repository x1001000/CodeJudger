total = 0               # 用total加總ASCII碼
for char in input():    # 對於輸入字串中的每個字元
    ASCII = ord(char)   # 字元的編碼（ASCII碼）
    total += ASCII      # 加入total
                        # 用雙引號寫f-string因為內含單引號
    print(f"ASCII code for '{char}' is {ASCII}")
print(total)