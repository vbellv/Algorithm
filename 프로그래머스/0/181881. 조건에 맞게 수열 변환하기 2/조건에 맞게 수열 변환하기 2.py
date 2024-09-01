def calculate_array(array):
    current = []
    
    for num in array:
        if num >= 50 and num % 2 == 0:
            num //= 2
        elif num < 50 and num % 2 != 0:
            num = num * 2 + 1
        else:
            num = num
        current.append(num)
    
    return current


def solution(arr):
    before = arr.copy()
    current = []
    number = 0
    
    while True:
        current = calculate_array(before)
            
        if before == current:
            return number
        else:
            number += 1
            before = current.copy()
            current = []
            
        