total = 0
for _ in range(5):
    card = input()
    if card == 'J':
        total += 11
    elif card == 'Q':
        total += 12
    elif card == 'K':
        total += 13
    elif card == 'A':
        total += 1
    else:
        total += int(card)
print(total)