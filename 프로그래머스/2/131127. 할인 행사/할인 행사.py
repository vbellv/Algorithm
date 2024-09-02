from collections import Counter

def make_product_dict(want, number):
    wants = dict()
    for product, count in zip(want, number):
        wants[product] = count
        
    return wants


def solution(want, number, discount):
    wants = make_product_dict(want, number)
    answer = 0
    
    for index in range(len(discount)):
        ten_days = dict(Counter(discount[index:index + 10]))
        
        if wants == ten_days:
            answer += 1
            
    return answer
