from functools import cmp_to_key

def compare(num1, num2):
    if num1 + num2 > num2 + num1:
        return -1
    elif num1 + num2 == num2 + num1:
        return 0
    else:
        return 1

    
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(compare))
    return str(int(''.join(numbers)))

print(solution([0, 0, 0]))   