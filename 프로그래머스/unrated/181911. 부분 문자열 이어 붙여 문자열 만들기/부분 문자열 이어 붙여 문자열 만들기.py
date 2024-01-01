def solution(my_strings, parts):
    answer = ''
    
    for idx in range(len(parts)):
        start, end = parts[idx][0], parts[idx][1]
        answer += my_strings[idx][start:end+1]
        
    return answer