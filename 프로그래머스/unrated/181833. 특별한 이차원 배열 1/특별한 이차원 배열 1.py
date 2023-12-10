def solution(n):
    arr = []
    
    for i in range(n):
        temp_arr = []
        
        for j in range(n):
            if i == j:
                temp_arr.append(1)
            else:
                temp_arr.append(0)
        arr.append(temp_arr)
    
    return arr