m = int(input())
n = int(input())

arr = [True] * (n+1)
arr[1] = False

answer = []

for i in range(2, int(n**0.5)+1):
    if arr[i]:
        for j in range(i+i, n+1, i):
            arr[j] = False
            
for num in range(m, n+1):
    if arr[num]:
        answer.append(num)
        
if not answer:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))