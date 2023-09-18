def num_split(polynomial):
    x_list, num_list = [], []
    
    polynomial = polynomial.split(' + ')
    
    for i in polynomial:
        if 'x' in i:
            x_list.append(i)
        else:
            num_list.append(i)
            
    return x_list, num_list

def sum_list(polynomial):
    x_list, num_list = num_split(polynomial)
    
    for i in range(len(x_list)):
        if 'x' == x_list[i]:
            x_list[i] = x_list[i].replace('x', '1')
        else:
            x_list[i] = x_list[i].replace('x', '')
            
    x_sum = sum(list(map(int, x_list)))
    num_sum = sum(list(map(int, num_list)))
    
    return x_sum, num_sum

def solution(polynomial):
    x_sum, num_sum = sum_list(polynomial)
            
    if num_sum > 0:
        if x_sum == 1:
            return 'x + ' + str(num_sum)
        elif x_sum == 0:
            return str(num_sum)
        else:
            return str(x_sum) + 'x + ' + str(num_sum) 

    # num_sum == 0
    else:  
        if x_sum != 1:
            return str(x_sum) + 'x'
        elif x_sum == 0:
            return 0
        else:
            return 'x'
        
            
print(solution('x'))
print(solution('1'))
print(solution('3x + x'))
print(solution('x + 1'))