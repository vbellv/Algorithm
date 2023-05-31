import sys
input = sys.stdin.readline

n = int(input())
num_list = sorted(list(int(input().rstrip()) for _ in range(n)))
print(*num_list, sep='\n')