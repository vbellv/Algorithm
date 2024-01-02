import sys
input = sys.stdin.readline

M, N = map(int, input().split())
boards = [list(map(str, input().strip())) for i in range(M)]
results = []

for i in range(M-8+1):
    for j in range(N-8+1):
        black_cnt = 0
        white_cnt = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if boards[a][b] != 'B':
                        black_cnt += 1
                    if boards[a][b] != 'W':
                        white_cnt += 1
                else:
                    if boards[a][b] != 'W':
                        black_cnt += 1
                    if boards[a][b] != 'B':
                        white_cnt += 1

        results.append(black_cnt)
        results.append(white_cnt) 
           
print(min(results))