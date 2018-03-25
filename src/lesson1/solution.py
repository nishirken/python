import sys
digit_string = sys.argv[1]
acc = 0

for symb in digit_string:
    acc += int(symb)

print(acc)
