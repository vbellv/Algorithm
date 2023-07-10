
def solution(clothes):
    clothes_dict = {}
    answer = 1
    
    for num in clothes:
        clothes_dict[num[1]] = 0
        
    for num in clothes:
        clothes_dict[num[1]] += 1
    
    for val in clothes_dict.values():
        answer *= (val + 1)
    
    return answer - 1