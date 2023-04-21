import sys
input = sys.stdin.readline

data = []
max_list = []

for _ in range(9):
    data.append(list(map(int, input().split())))

for i in range(9):
    max_list.append(max(data[i]))

max_num = max(max_list)

for i in range(9):
    for j in range(9):
        if max_num == data[i][j]:
            print(max_num)
            print(i+1, j+1)