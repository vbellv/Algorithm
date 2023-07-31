import sys
input = sys.stdin.readline

sum_money, left_money = map(int, input().split())

print(sum_money // left_money)
print(sum_money % left_money)