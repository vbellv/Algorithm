n = int(input())
money = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    
    if a == b == c:
        if money < 10000+a*1000:
            money = 10000+a*1000
    elif a != b and b != c and c != a:
        if money < max(a, b, c) * 100:
            money = max(a, b, c) * 100
    else:
        if a == b:
            if money < 1000+a*100:
                money = 1000+a*100
        elif c == b:
            if money < 1000+b*100:
                money = 1000+b*100
        elif a == c:
            if money < 1000+c*100:
                money = 1000+c*100

print(money)