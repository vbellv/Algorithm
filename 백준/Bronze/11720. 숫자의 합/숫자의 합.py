import sys
input = sys.stdin.readline

n = int(input())
num = str(input())

sum_num = 0

for i in range(n):
    sum_num += int(num[i])
    
print(sum_num)