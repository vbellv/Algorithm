def solution(sizes):
    sizes = list(sorted(i) for i in sizes)
    
    return max([i[0] for i in sizes]) * max([i[1] for i in sizes])