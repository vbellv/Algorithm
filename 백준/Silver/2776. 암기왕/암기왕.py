import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    note1 = sorted(list(map(int, input().split())))
    m = int(input())
    note2 = list(map(int, input().split()))

    def search(note1, check):
        start = 0
        end = len(note1) - 1
        while start <= end:
            mid = (start + end) // 2
            if note1[mid] == check:
                return 1
            elif note1[mid] > check:
                end = mid - 1
            else:
                start = mid + 1
        return 0

    for check in note2:
        print(search(note1, check))