def solution(my_string):
    my_string = sorted([i for i in my_string.lower()])
    return ''.join(my_string)