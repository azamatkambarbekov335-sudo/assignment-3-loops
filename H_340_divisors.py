x = int(input())
small = []
large = []
i = 1
while i * i <= x:
    if x % i == 0:
        small.append(i)
        if i != x // i:
            large.append(x // i)
    i += 1
print(*(small + large[::-1]))
