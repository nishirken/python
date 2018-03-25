import sys
from math import sqrt
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b ** 2 - 4 * a * c
x1 = None
x2 = None

if D > 0:
    x1 = (- b - sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (- b + sqrt(b ** 2 - 4 * a * c)) / 2 * a
elif D == 0:
    x1 = x2 = - b / 2 * a

print(int(x1))
print(int(x2))

