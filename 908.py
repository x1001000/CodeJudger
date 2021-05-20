# 開檔，每一行的每一個字存入words
words = []
with open(input()) as f:
    for line in f.readlines():
        words += line.split()
        # 若用words.append()方法
        # 會將line.split()傳出的串列
        # 當成一個東西加到words最後一項

# 一一比對words中的每一個word長度是否為n
# 若為n則加入match_words集合
n = int(input())
match_words = set()
for word in words:
    if words.count(word) == n:
        match_words.add(word)

# sorted(match_words)是排序過的match_words
# 若match_words中的元素是字串
# 則用字串的第一個字元的編碼排序
# 預設為由小至大
for match_word in sorted(match_words):
    print(match_word)