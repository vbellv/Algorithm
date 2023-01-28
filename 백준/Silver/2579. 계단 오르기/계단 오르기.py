import sys
input = sys.stdin.readline

n = int(input())
steps = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

def sol(n):
    if n == 1:
        return steps[0]
    elif n == 2:
        return steps[0] + steps[1]
    else:
        dp[0] = steps[0]
        dp[1] = steps[0] + steps[1]
        dp[2] = max(steps[0], steps[1]) + steps[2]
        for i in range(3, n):
            dp[i] = max(dp[i-2] + steps[i], dp[i-3] + steps[i-1] + steps[i])
        return dp[n-1]
        
print(sol(n))