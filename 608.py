data = [int(input()) for _ in range(9)]
M = max(data)
m = min(data)
print(f'Index of the largest number {M} is: ({data.index(M)//3}, {data.index(M)%3})')
print(f'Index of the smallest number {m} is: ({data.index(m)//3}, {data.index(m)%3})')