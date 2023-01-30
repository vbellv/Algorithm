import sys
input = sys.stdin.readline

n = int(input())
card_nums = sorted(list(map(int, input().split())))
m = int(input())
check_nums = list(map(int, input().split()))

def check(card_nums, checks):
    start = 0
    end = len(card_nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if card_nums[mid] == checks:
            return 1
        elif card_nums[mid] > checks:
            end = mid - 1
        else:
            start = mid + 1
    return

for i in range(m):
    if check(card_nums, check_nums[i]) == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')