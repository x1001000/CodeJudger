while True:
    H = float(input())
    if H == -9999:
        break
    else:
        W = float(input())
        BMI = W / (H/100)**2
        print(f'BMI: {BMI:.2f}')
        if BMI < 18.5:
            print("State: under weight")
        if 18.5 <= BMI < 25:
            print("State: normal")
        if 25.0 <= BMI < 30:
            print("State: over weight")
        if 30 <= BMI:
            print("State: fat")