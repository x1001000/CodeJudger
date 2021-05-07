# 這題寫這樣不會過，雖然輸出都對
# print(int(input())*int(input()))

# 但寫這樣就會過，程式碼裡面有def compute
# print(int(input())*int(input()))
# # def compute

# 因為CJ除了比對輸出
# 還檢查程式碼裡面有沒有def compute
# 題意是要求你寫這樣
def compute(x, y):
    return x * y
print(compute(int(input()), int(input())))