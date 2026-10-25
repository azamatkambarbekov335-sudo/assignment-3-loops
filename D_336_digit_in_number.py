import sys

x, d = map(int, sys.stdin.read().split())
count = 0
while x > 0:
    if x % 10 == d:
        count += 1
    x //= 10
print(count)
