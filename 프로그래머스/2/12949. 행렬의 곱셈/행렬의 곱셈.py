def new_arr(arr2):
    new_arr2 = []
    
    for col in range(len(arr2[0])):
        temp = []
        
        for row in range(len(arr2)):
            temp.append(arr2[row][col])
        new_arr2.append(temp)
        
    return new_arr2

def solution(arr1, arr2):
    answer = []
    arr2 = new_arr(arr2)
    
    for num1 in arr1:
        temp_arr = []
        
        for num2 in arr2:
            temp_num = 0
            
            for idx in range(len(num1)):
                temp_num += num1[idx] * num2[idx]
            temp_arr.append(temp_num)
            
        answer.append(temp_arr)
        
    return answer
