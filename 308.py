for _ in range(int(input())):
    x = input()
    y = 0
    for i in x:
        y += int(i) # y = y + int(i)
    print(f'Sum of all digits of {x} is {y}')