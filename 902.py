with open('read.txt') as f:
    print(sum(map(int, f.readline().split())))