import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
d = [a, b, c]

if a == b == c:
    print(10000 + a * 1000)
elif a == b or b == c or c == a:
    if a == b:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + b * 100)
    else:
        print(1000 + c * 100)
elif a != b != c:
    if max(d) == a:
        print(a * 100)
    elif max(d) == b:
        print(b * 100)
    elif max(d) == c:
        print(c * 100)