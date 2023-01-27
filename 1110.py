n = int(input())

def cycle_1(n):
    num = 0
    plus_n = n // 10 + n % 10
    new_n = (n % 10) * 10 + (plus_n % 10)
    num += 1
    return plus_n, new_n, num, n

def cycle_2(n):
    plus_n, new_n, num, n = cycle_1(n)

    while new_n != n:
        plus_n = new_n // 10 + new_n % 10
        new_n = (new_n % 10) * 10 + (plus_n % 10)
        num += 1
    return num

print(cycle_2(n))