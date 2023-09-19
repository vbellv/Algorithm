def solution(n):
    except_three_list = []
    num = 0
    
    while len(except_three_list) <= 100:
        if num % 3 != 0 and '3' not in str(num):
            except_three_list.append(num)
        
        num += 1
        
    return except_three_list[n-1]
    