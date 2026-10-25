import sys

data = sys.stdin.read().split()
n = int(data[0])
zeros = 0
for i in range(1, n + 1):
    if int(data[i]) == 0:
        zeros += 1
print(zeros)
