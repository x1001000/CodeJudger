# set和dict都使用大括號
# 但{}是空的dict
# 所以空的set要用set()生
numbers = set()

while True:
    number = int(input())
    if number == -9999:
        break
    else:
        numbers.add(number)

print(f'Length: {len(numbers)}')
print(f'Max: {max(numbers)}')
print(f'Min: {min(numbers)}')
print(f'Sum: {sum(numbers)}')