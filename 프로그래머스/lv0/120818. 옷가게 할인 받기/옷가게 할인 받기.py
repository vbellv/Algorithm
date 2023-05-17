def solution(price):
    import math
    if price < 100000:
        answer = price
    elif (price >= 100000) & (price < 300000):
        answer = price * (1-0.05)
    elif (price >= 300000) & (price < 500000):
        answer = price * (1-0.1)
    else:
        answer = price * (1-0.2)
    return math.floor(answer)