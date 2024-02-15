import sys
input = sys.stdin.readline

n = int(input())
check_numbers = [0] * (10000+1)

for _ in range(n):
    check_numbers[int(input())] += 1

for i in range(len(check_numbers)):
    if check_numbers[i] != 0:
        for _ in range(check_numbers[i]):
            print(i)