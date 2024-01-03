def solution(my_string, m, c):
    return ''.join([my_string[num] for idx, num in enumerate(range(len(my_string))) if idx % m == c-1])