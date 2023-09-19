def solution(n):
    except_three_list = []
    num = 0
    
    while True:
        if num % 3 != 0 and '3' not in str(num):
            except_three_list.append(num)
        
        num += 1
        
        if len(except_three_list) == 100:
            break
        
    return except_three_list[n-1]
    