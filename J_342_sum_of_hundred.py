import sys

numbers = sys.stdin.read().split()
total = 0
for i in range(100):
    total += int(numbers[i])
print(total)
