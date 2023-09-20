def solution(dots):
    x1, y1, x2, y2 = dots[0][0], dots[0][1], 0, 0
    
    for i in dots:
        if x1 != i[0]: x2 = i[0]
        elif y1 != i[1]: y2 = i[1]
        
    return (max(x1, x2) - min(x1, x2)) * (max(y1, y2) - min(y1, y2))