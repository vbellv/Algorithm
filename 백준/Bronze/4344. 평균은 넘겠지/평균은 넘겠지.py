import sys
input = sys.stdin.readline

n = int(input())

for idx in range(n):
    student = list(map(int, input().split()))
    average = sum(student[1:]) / student[0]
    
    cnt = 0
    for score in student[1:]:
        if score > average:
            cnt += 1
    print(f'{round((cnt / student[0]) * 100, 3):.3f}%')