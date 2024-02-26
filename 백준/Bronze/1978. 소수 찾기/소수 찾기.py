n = int(input())
numbers = sorted(list(map(int, input().split())))
cnt = 0

arr = [True] * (numbers[-1]+1)
arr[1] = False

for i in range(2, int(numbers[-1]**0.5)+1):
    if arr[i]:
        for num in range(i+i, numbers[-1]+1, i):
            arr[num] = False

for i in range(1, len(arr)):
    if arr[i] and i in numbers:
        cnt += 1
print(cnt)