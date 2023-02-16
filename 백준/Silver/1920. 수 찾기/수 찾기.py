import sys
input = sys.stdin.readline

n = int(input())
num_n = sorted(list(map(int, input().split())))
m = int(input())
num_m = list(map(int, input().split()))

def check(num_n, data):
    start = 0
    end = len(num_n) - 1
    while start <= end:
        mid = (start + end) // 2
        if num_n[mid] == data:
            return 1
        elif num_n[mid] > data:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in num_m:
    print(check(num_n, i))