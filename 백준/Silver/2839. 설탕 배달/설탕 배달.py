n = int(input())
num = max(n//5+1, n//3+1)
arr = [[0 for _ in range(num)] for _ in range(num)]
answer = 9999999

for i in range(num):
    for j in range(num):
        if i*3 + j*5 <= n:
            arr[i][j] = i*3 + j*5
        else:
            arr[i][j] = arr[i-1][j-1]
        
for i in range(num):
    for j in range(num):
        if arr[i][j] == n:
            if answer > i+j:
                answer = i+j

if answer == 9999999:
    print(-1)
else:
    print(answer)