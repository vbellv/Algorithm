def solution(arr, k):
    stack = []
    
    for number in arr:
        if number not in stack:
            stack.append(number)

        if len(stack) == k:
            break
    
    return stack + [-1] * (k - len(stack))
