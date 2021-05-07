def compute(n):
    Fibonacci_numbers = F = [0, 1]
    for _ in range(n-2):
        F.append(F[-2] + F[-1])
    return F

num = int(input())
        #compute(n=num)的n=可以省略不寫
for i in compute(num):
    print(i, end=' ')