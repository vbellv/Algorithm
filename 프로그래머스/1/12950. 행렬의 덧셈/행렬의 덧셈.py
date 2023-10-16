def solution(arr1, arr2):
    arr_ans = []
    
    for i in range(len(arr1)):
        temp_ans = []
        for j in range(len(arr1[i])):
            temp_ans.append(arr1[i][j] + arr2[i][j])
            
        arr_ans.append(temp_ans)
        
    return arr_ans