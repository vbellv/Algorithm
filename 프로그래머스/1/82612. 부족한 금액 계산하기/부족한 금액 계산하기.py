def solution(price, money, count):
    check_money = sum([price*num for num in range(1, count+1)])
    
    return check_money-money if check_money > money else 0
