def solution(strArr):
    return [strArr[idx].lower() if idx % 2 == 0 else strArr[idx].upper() for idx in range(len(strArr))]