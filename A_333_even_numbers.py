import sys

a, b = map(int, sys.stdin.read().split())
start = a if a % 2 == 0 else a + 1
result = []
for i in range(start, b + 1, 2):
    result.append(i)
print(*result)
