num = int(input())
if num < 10:
    print(num)
else: # 10~15印出A~F
    print(chr(ord('A') + num - 10))

# ord() 和 chr() 看 Paper 3/18
# 如果第5行看不懂，就註解掉第4,5行，反註解以下全部
# if num == 10:
#     print('A')
# if num == 11:
#     print('B')
# if num == 12:
#     print('C')
# if num == 13:
#     print('D')
# if num == 14:
#     print('E')
# if num == 15:
#     print('F')