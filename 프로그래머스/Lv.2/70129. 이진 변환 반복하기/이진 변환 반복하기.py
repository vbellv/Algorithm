def solution(s):
    convert_cnt, zero_cnt = 0, 0
    
    while True:
        zero_cnt += s.count('0')
        s = s.replace('0', '')
        
        s = bin(len(s))[2:]
        convert_cnt += 1
        
        if s == '1':
            break
    
    return [convert_cnt, zero_cnt]