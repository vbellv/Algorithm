def solution(str1, str2):
    return ''.join(str1[idx]+str2[idx] for idx in range(len(str1)))