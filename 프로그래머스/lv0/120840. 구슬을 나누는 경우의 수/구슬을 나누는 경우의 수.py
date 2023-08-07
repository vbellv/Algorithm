from math import factorial as F

def solution(balls, share):
    return F(balls) // (F(balls-share) * F(share))