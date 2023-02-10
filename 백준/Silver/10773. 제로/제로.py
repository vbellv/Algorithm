import sys
input = sys.stdin.readline

k = int(input())
nums = [int(input()) for _ in range(k)]
stack = []

for num in nums:
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))