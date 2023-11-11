def solution(num_list):
    if sorted(num_list)[0] < 0:
        for idx, num in enumerate(num_list):
            if num < 0:
                return idx
                break
    else:
        return -1        