import sys

data = sys.stdin.read().split()
n = int(data[0])
answer = "NO"
for i in range(1, n + 1):
    if int(data[i]) == 0:
        answer = "YES"
        break
print(answer)
