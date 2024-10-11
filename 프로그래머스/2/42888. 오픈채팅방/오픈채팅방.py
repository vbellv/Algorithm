def make_user_dict(record):
    user_dict = {}
    
    for sentence in record:
        sentence = sentence.split(' ')
        if sentence[0] != 'Leave':
            user_dict[sentence[1]] = sentence[2]
    
    return user_dict
    
def solution(record):
    user_dict = make_user_dict(record)
    answer = []
    
    for sentence in record:
        sentence = sentence.split(' ')
        
        if sentence[0] == 'Enter':
            answer.append(f'{user_dict[sentence[1]]}님이 들어왔습니다.')
        elif sentence[0] == 'Leave':
            answer.append(f'{user_dict[sentence[1]]}님이 나갔습니다.')
            
    return answer
            