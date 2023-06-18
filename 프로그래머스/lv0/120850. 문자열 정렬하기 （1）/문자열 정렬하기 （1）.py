def solution(my_string):
    num_list = [str(i) for i in range(10)]
    answer = [int(num) for num in my_string if num in num_list]
    return sorted(answer)