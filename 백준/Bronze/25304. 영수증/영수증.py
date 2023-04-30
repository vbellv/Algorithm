import sys
input = sys.stdin.readline

total = int(input())
n = int(input())

check_sum = 0

for _ in range(n):
    product, num = map(int, input().split())
    check_sum += product * num

if check_sum == total:
    print('Yes')
else:
    print('No')