# 全部小寫英文字母的一個集合
letters = set('abcdefghijklmnopqrstuvwxyz')
# 輸入指定次數
for _ in range(int(input())):
    # input().lower().replace(' ', '')
    # 輸入字串中的大寫轉小寫 空白移除 然後轉成一個集合
    # 印出兩個集合的比較結果 Ture 或 False
    print(letters == set(input().lower().replace(' ', '')))