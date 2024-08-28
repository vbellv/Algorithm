def solution(arr):
    stack = []
    
    for i in range(len(arr)):
        if stack and stack[-1] == arr[i]:
            stack.pop()
        else:
            stack.append(arr[i])
    
    return stack if stack else [-1]
