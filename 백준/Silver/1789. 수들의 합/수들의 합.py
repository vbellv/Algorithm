n = int(input())
sum, max = 0, 0

for i in range(1, n+1):
    sum += i
    max = i
    if sum > n:
        max -= 1
        break

print(max)