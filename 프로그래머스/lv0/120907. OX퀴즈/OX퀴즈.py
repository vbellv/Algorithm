def solution(quiz):
    answer = []
    
    for num in quiz:
        math = num.replace('=', '==')
        
        if eval(math):
            answer.append("O")
        else:
            answer.append("X")
            
    return answer