def solution(n):
    answer = []
    
    for num in range(2, n+1):
        if n % num == 0:
            if (num % 2 != 0) and (num % 3 != 0) and (num % 5 != 0) and (num % 7 != 0):
                if n == num:
                    if len(answer) == 0:
                        answer.append(num)
                else:
                    answer.append(num)
            if num == 2 or num == 3 or num == 5 or num == 7:
                answer.append(num)
                
    return answer

print(solution(121))