x = int(input())
answer = x
i = 2
while i * i <= x:
    if x % i == 0:
        answer = i
        break
    i += 1
print(answer)
