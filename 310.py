n = int(input())
answer = 0
for i in range(1, n): # i依序代入1到n-1
    answer += 1 / (i**0.5 + (i+1)**0.5)
print(f'{answer:.4f}')