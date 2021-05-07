data = []
for week in range(4):
    print(f'Week {week+1}:')
    for day in range(3):
        T = input(f'Day {day+1}:')
        # 全部轉整數會炸 全部轉浮點數印出會錯(多餘的.0)
        try:    # 可以轉整數的 轉整數
            data.append(int(T))
        except: # 無法轉整數的 轉浮點數
            data.append(float(T))
print(f'Average: {sum(data)/len(data):.2f}')
print(f'Highest: {max(data)}')
print(f'Lowest: {min(data)}')