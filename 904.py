names, heights, weights = [], [], []

with open('read.txt') as f:
    for line in f.readlines():
        print(line)
        name, height, weight = line.split()
        names.append(name)
        heights.append(float(height))
        weights.append(float(weight))

n = len(names)  # n個人
H = max(heights)# 最高H
W = max(weights)# 最重W

print(f'Average height: {sum(heights)/n:.2f}')
print(f'Average weight: {sum(weights)/n:.2f}')
print(f'The tallest is {names[heights.index(H)]} with {H:.2f}cm')
print(f'The heaviest is {names[weights.index(W)]} with {W:.2f}kg')