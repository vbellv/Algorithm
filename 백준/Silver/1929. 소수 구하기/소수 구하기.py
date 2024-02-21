n, m = map(int, input().split())

check = [True] * (m+1)
check[1] = False

for i in range(2, int(m**0.5)+1):
    if check[i] == True:
        for j in range(i+i, m+1, i):
            check[j] = False

for i in range(n, m+1):
    if check[i] == True:
        print(i)