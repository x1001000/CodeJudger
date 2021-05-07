data = []
data_count = []
# 十個整數讀進data
for _ in range(10):
    data.append(int(input()))
# 每個整數在十個整數中共出現幾次記錄在data_count
for item in data:
    data_count.append(data.count(item))
# 找出眾數出現的次數及其索引值
count = max(data_count)
index = data_count.index(count)
# 印出眾數及眾數出現的次數
print(data[index])
print(count)