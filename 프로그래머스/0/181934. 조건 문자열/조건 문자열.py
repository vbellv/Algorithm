def solution(ineq, eq, n, m):
    sign = ineq + eq
    if sign == '>=':
        if n >= m:
            return 1
    elif sign == '<=':
        if n <= m:
            return 1
    elif sign == '>!':
        if n > m:
            return 1
    elif sign == '<!':
        if n < m:
            return 1
    return 0