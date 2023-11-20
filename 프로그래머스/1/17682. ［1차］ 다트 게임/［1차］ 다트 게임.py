def solution(dartResult):
    answer = []
    score = ''
    score_dict = {'S': 1, 'D': 2, 'T': 3}
    
    for word in dartResult:
        # 숫자인 경우는 score에 저장
        if word.isdigit():
            score += word
        
        # S, D, T 계산 처리하기
        elif word in score_dict:
            answer.append(int(score) ** score_dict[word])
            score = ''
        
        # #인 경우 answer에 저장된 마지막 값을 -1 곱해주기
        elif word == '#':
            answer[-1] *= -1
        
        # *인 경우 answer에 저장된 마지막 값에 2 곱해주기
        elif word == '*':
            answer[-1] *= 2
            
            # 만약 기존에 저장된 answer의 길이가 2 이상인 경우는 뒤에서 두번째 값도 2 곱해주기
            if len(answer) >= 2:
                answer[-2] *= 2
                
    return sum(answer)