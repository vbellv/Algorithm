from itertools import combinations

def solution(number):
    cnt = 0
    students = list(combinations(number, 3))
    
    for nums in students:
        if sum(nums) == 0:
            cnt += 1
            
    return cnt