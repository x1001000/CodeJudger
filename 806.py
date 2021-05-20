# 應題目要求定義compute函數，傳遞兩字串，傳回一整數
def compute(str1, str2):
    return str1.count(str2)

line1 = input()
line2 = input()

print(f'{line2} occurs {compute(line1, line2)} time(s)')