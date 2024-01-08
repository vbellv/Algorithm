from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    total_list = []
    
    for i in range(1, len(numbers)+1):
        com = list(permutations(numbers, i))
        for nums in com:
            total_list.append(''.join(nums))
    
    total_list = list(set(list(map(int, total_list))))
    total_list = list(num for num in total_list if num > 1)
    
    not_in_list = []
    
    for num in total_list:
        for check in range(2, int(num ** 0.5)+1):
            if num % check == 0:
                not_in_list.append(num)
    
    return len([num for num in total_list if num not in not_in_list])