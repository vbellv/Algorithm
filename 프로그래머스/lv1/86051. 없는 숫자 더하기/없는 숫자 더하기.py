def solution(numbers):
    num_list = [i for i in range(10)]
    return sum([i for i in num_list if i not in numbers])