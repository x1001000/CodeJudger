for _ in range(int(input())):
    # map是數學的映射的意思，map函數的用法是
    # map(轉換函數, 原始串列)傳出map物件
    # map物件轉list物件，即串列
    # 串列中的每一項就是原始串列中的每一項一一透過轉換函數得來
    numbers = list(map(float, input().split()))
    # 差值 = 最大值 - 最小值
    answer = max(numbers) - min(numbers)
    # 差值輸出到小數點後第二位
    print(f'{answer:.2f}')