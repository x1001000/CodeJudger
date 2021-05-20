# 男生人數和女生人數初始值皆設為0
N_males = N_females = 0
with open('read.dat') as f:
    for line in f.readlines():
        print(line)
        N = line.split()[-2]
        # 排除檔案第一行切出來的N為'性別'的情況
        if N == '0':
            N_females += 1
        if N == '1':
            N_males += 1
print(f'Number of males: {N_males}')
print(f'Number of females: {N_females}')