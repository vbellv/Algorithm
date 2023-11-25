def solution(a, b, n):
    answer, remainder = 0, 0
    
    while n > 1:
        n, r = divmod(n, a)
        
        answer += n * b
        n *= b
        remainder += r
        
        if n <= a:
            n += remainder
            remainder = 0

            if n >= a:
                continue
            else:
                break

    return answer