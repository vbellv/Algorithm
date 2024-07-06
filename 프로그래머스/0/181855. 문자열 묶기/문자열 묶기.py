def solution(strArr):
    length = [0] * 31
    
    for word in strArr:
        length[len(word)] += 1
        
    return max(length)