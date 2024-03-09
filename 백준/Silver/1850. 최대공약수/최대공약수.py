n, m = map(int, input().split())

def gcd(x, y):
    if y == 0:
        print(x * '1')
        return
    else:
        return gcd(y, x%y)

gcd(max(n, m), min(n, m))