import sys
input = sys.stdin.readline

n = int(input())
num_list = sorted(list(int(input().rstrip()) for _ in range(n)))

for num in num_list:
    print(num)