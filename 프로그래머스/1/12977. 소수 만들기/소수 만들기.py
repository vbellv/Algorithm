from itertools import combinations

def prime_check(number):
    for num in range(2, int(number**0.5)+1):
        if number % num == 0:
            return False
    return True

def solution(nums):
    prime_nums = []
    comb_list = list(combinations(nums, 3))
    
    for numbers in comb_list:
        if prime_check(sum(numbers)):
            prime_nums.append(sum(numbers))
    
    return len(prime_nums)