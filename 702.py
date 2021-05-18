numbers = []

for t in range(2):
    print(f'Create tuple{t+1}:')
    while True:
        number = int(input())
        if number == -9999:
            break
        else:
            numbers.append(number)

print(f'Combined tuple before sorting: {tuple(numbers)}')
print(f'Combined list after sorting: {sorted(numbers)}')