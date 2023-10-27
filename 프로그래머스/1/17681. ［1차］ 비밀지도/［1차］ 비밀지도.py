def arr(n, arr_num):
    arr = []
    base = ''
    
    for num in arr_num:
        while num > 0:
            num, mod = divmod(num, 2)
            base += str(mod)
        
        if len(base) < n:
            base = base + (n - len(base)) * '0'
        arr.append(list(map(int, base[::-1])))
        base = ''
    
    return arr

def solution(n, arr1, arr2):
    arr1 = arr(n, arr1)
    arr2 = arr(n, arr2)
    
    answer = []
    
    for list1, list2 in zip(arr1, arr2):
        temp_str = ''
        for num1, num2 in zip(list1, list2):
            if num1 or num2 == 1:
                temp_str += '#'
            elif num1 == 0 and num2 == 0:
                temp_str += ' '
        answer.append(temp_str)
        
    return answer