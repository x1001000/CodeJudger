# 三個輸入存入串列X
X = int(input()), int(input()), int(input())
# 串列X排序成小中大依序存入S M L
S, M, L = sorted(X)
# 三角形必定：小+中>大
if S + M > L:
    print(sum(X))
else:
    print('Invalid')