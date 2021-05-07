n = int(input())
X = 1       # 因為要連乘，所以初始值設為1
for i in range(1, n+1): # i依序代入1到n
    X *= i              # X = X * i
print(X)