def start_and_barriers(park):
    n = len(park)
    m = len(park[0])
    
    barriers = []
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                start = [i, j]
            if park[i][j] == 'X':
                barriers.append((i, j))
                
    return start, barriers

def is_valid(park, x, y):
    n = len(park)
    m = len(park[0])
    return 0 <= x < n and 0 <= y < m

def can_move(start, end, barriers):
    x, y = start
    nx, ny = end

    if x == nx:
        for i in range(min(y, ny), max(y, ny) + 1):
            if (x, i) in barriers:
                return False
    elif y == ny:
        for i in range(min(x, nx), max(x, nx) + 1):
            if (i, y) in barriers:
                return False
    return True
    
def solution(park, routes):
    start, barriers = start_and_barriers(park)
    
    for route in routes:
        op, n = route.split()
        move = start.copy()
        
        if op == 'N':
            move[0] -= int(n)
        elif op == 'S':
            move[0] += int(n)
        elif op == 'W':
            move[1] -= int(n)
        else:
            move[1] += int(n)
            
        if is_valid(park, move[0], move[1]) and can_move(start, move, barriers):
            start = move

    return start
