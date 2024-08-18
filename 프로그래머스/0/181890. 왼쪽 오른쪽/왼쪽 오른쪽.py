def solution(str_list):
    words = ''.join(str_list)
    l_index = words.find('l')
    r_index = words.find('r')

    if l_index != -1 and r_index != -1:
        if l_index < r_index:
            return str_list[:l_index]
        else:
            return str_list[r_index + 1:]
        
    elif l_index != -1 and r_index == -1:
        return str_list[:l_index]
    
    elif l_index == -1 and r_index != -1:
        return str_list[r_index + 1:]
    
    elif l_index == -1 and r_index == -1:
        return []
