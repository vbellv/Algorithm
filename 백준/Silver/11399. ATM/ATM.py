n = int(input())
times = sorted(list(map(int, input().split())))

time_sum = [0] * (n+1)
time_sum[1] = times[0]

for i in range(2, n+1):
    time_sum[i] = time_sum[i-1] + times[i-1]
    
print(sum(time_sum))