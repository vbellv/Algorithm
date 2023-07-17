def solution(array):
    answer = [int(i) for arr in array for i in str(arr)]
    return answer.count(7) 