import string

def solution(age):
    return ''.join([string.ascii_lowercase[int(i)] for i in str(age)])