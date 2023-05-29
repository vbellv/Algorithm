import sys
input = sys.stdin.readline

# 2차원 배열 초기화
white_paper = [[0 for j in range(101)] for i in range(101)]
black_paper = 10

n = int(input())
for _ in range(n):
    col, row = map(int, input().split())
    col = col-1
    row = row-1
    
    for i in range(col, col+black_paper):
        for j in range(row, row+black_paper):
            white_paper[i][j] = 1
    
cnt = 0
for i in range(101):
    for j in range(101):
        if white_paper[i][j] == 1:
            cnt += 1
print(cnt)