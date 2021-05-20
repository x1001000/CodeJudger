line = input()          # 輸入一行字存入line
print(line.upper())     # 整行變大寫印出
Line = []               # 用串列Line存每個單字
for word in line.split():
                        # 每個單字的字首變大寫接上其餘部分
    Line.append(word[0].upper()+word[1:])
print(' '.join(Line))   # 用一個空格把串列Line接成一字串