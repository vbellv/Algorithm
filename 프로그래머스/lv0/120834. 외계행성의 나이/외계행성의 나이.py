# def solution(age):
#     import string
#     return ''.join([string.ascii_lowercase[int(i)] for i in str(age)]) 

def solution(age):
    return ''.join([chr(int(i)+97) for i in str(age)])