while True:
    try:
        n, m = map(int, input().split())
        if m % n == 0:
            print('factor')
        elif n % m == 0:
            print('multiple')
        else:
            print('neither')
    except:
        break