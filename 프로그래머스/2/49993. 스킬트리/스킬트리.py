def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        check = ''
        for word in skills:
            if word in skill:
                check += word
        
        if skill.startswith(check):
            answer += 1
            
    return answer
