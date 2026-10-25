import sys

data = sys.stdin.read().split()
n = int(data[0])
zeros = positive = negative = 0
for i in range(1, n + 1):
    value = int(data[i])
    if value == 0:
        zeros += 1
    elif value > 0:
        positive += 1
    else:
        negative += 1
print(zeros, positive, negative)
