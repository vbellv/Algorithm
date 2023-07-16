import re

def solution(my_string):
    num_list = re.findall(r'\d+', my_string)
    return sum(list(map(int, num_list)))