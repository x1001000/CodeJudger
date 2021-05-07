a = int(input())
b = int(input())
op = input()
if op == '+':
    print(a + b)
if op == '-':
    print(a - b)
if op == '*':
    print(a * b)
if op == '/':
    print(a / b)
if op == '//':
    print(a // b)
if op == '%':
    print(a % b)

# 也可以用eval函數解這題，知道就好，不要用
# eval將字串變程式碼，太危險，所以實際開發絕不使用
# a = input()
# b = input()
# op = input()
# print(eval(a+op+b))