import sys

a, b, c, d = map(int, sys.stdin.read().split())
result = []
for i in range(a, b + 1):
    if i % d == c:
        result.append(i)
print(*result)
