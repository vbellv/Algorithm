def solution(order):
    result = 0
    for drink in order:
        if 'latte' in drink:
            result += 5000
        elif 'americano' or 'anything' in drink:
            result += 4500
            
    return result
    