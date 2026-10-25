import sys

data = sys.stdin.read().split()
n = int(data[0])
total = 0
for i in range(1, n + 1):
    total += int(data[i])
print(total)
