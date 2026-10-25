import sys

a, b, c, d, e = map(int, sys.stdin.read().split())
count = 0
for x in range(0, 1001):
    if x != e and a * x ** 3 + b * x ** 2 + c * x + d == 0:
        count += 1
print(count)
