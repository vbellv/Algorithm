import sys
input = sys.stdin.readline

NUMBER = 5
num_list = [int(input().rstrip()) for _ in range(NUMBER)]

avarage = sum(num_list) // NUMBER
median = sorted(num_list)[(NUMBER)//2]

print(avarage)
print(median)