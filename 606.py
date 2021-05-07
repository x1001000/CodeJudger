rows = int(input())
cols = int(input())
for row in range(rows):
    print(''.join([f'{col-row:4d}' for col in range(cols)]))
# def compute CJ笨笨