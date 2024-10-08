from itertools import permutations

def solution(k, dungeons): 
    answer = 0
    dungeons_cases = list(permutations(dungeons, len(dungeons)))
    
    for dungeons in dungeons_cases:
        count = 0
        number = k
        for dungeon in dungeons:
            if dungeon[0] <= number:
                count += 1
                number -= dungeon[1]
        
        if answer <= count:
            answer = count
            
    return answer
