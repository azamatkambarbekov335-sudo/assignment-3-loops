n = int(input())
result = []
value = 1
while len(result) < n:
    for _ in range(value):
        if len(result) == n:
            break
        result.append(value)
    value += 1
print(*result)
