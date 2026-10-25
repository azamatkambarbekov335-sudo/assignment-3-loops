import sys
from math import isqrt

a, b = map(int, sys.stdin.read().split())
result = []
i = isqrt(max(a, 0))
if i * i < a:
    i += 1
while i * i <= b:
    result.append(i * i)
    i += 1
print(*result)
