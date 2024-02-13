areas = [list(map(int, input().split())) for _ in range(4)]
total_areas = [[0] * 100 for _ in range(100)]
cnt = 0

for i in range(4):
    left_x, left_y, right_x, right_y = areas[i]
    
    for x in range(left_x, right_x):
        for y in range(left_y, right_y):
            total_areas[x][y] = 1
            
for i in range(100):
    for j in range(100):
        if total_areas[i][j] != 0:
            cnt += 1
print(cnt)