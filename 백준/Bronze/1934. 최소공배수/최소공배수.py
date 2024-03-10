def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    gcd_num = gcd(max(x, y), min(x, y))
    print(x//gcd_num * y//gcd_num * gcd_num)