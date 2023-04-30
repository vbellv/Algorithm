import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    data = str(input()).strip()
    num = 0
    sum_num = 0
    for i in range(len(data)):
        if data[i] == 'O':
            num += 1
            sum_num += num
        else:
            num = 0
    print(sum_num)