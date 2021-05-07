a = int(input())
b = int(input())
X = 0
# range(start, stop, step) 看Paper 4/22
for i in range(a, b+1): # i依序代入a到b
    if i % 2 == 0:      # 若i為偶數
        X += i          # X = X + i
print(X)