def solution(arr, k):
    stack = []
    
    for number in arr:
        if number not in stack:
            stack.append(number)

        if len(stack) == k:
            return stack
    
    if len(stack) != k:
        return stack + [-1] * (k - len(stack))