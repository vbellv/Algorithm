def solution(sizes):
    sizes = list(sorted(i) for i in sizes)
    
    left_num = [i[0] for i in sizes]
    right_num = [i[1] for i in sizes]
    
    return max(left_num) * max(right_num)