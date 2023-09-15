def solution(quiz):
    answer = []
    
    for num in quiz:
        math = num.split('=')[0]
        math_ans = num.split('=')[1]
        
        if eval(math) == int(math_ans):
            answer.append("O")
        else:
            answer.append("X")
    
    return answer