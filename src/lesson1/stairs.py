import sys
num_steps = int(sys.argv[1])


for step in range(num_steps + 1):
    if step == 0:
        continue

    if step == num_steps:
        print('#' * step)
        break

    print(' ' * (num_steps - step - 1), '#' * step)


