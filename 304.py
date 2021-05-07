a = int(input())
X = 0
# range(start, stop, step) 看Paper 4/22
for i in range(1, a+1): # i依序代入1到a
    if i % 5 == 0:      # 若i為5之倍數
        X += i          # X = X + i
print(X)