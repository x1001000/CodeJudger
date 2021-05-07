even = odd = 0

for _ in range(10):
    if int(input()) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'Even numbers: {even}')
print(f'Odd numbers: {odd}')