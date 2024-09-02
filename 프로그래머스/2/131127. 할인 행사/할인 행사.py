from collections import Counter

def make_product_dict(want, number):
    wants = dict()
    for product, count in zip(want, number):
        wants[product] = count
    
    wants = dict(sorted(wants.items(), key=lambda x: (x[1], x[0]), reverse=True))
    
    return wants


def solution(want, number, discount):
    wants = make_product_dict(want, number)
    answer = 0
    
    for index in range(len(discount)):
        ten_days = dict(Counter(discount[index:index + 10]))
        ten_days = dict(sorted(ten_days.items(), key=lambda x: (x[1], x[0]), reverse=True))
        
        if wants == ten_days:
            answer += 1
            
    return answer
