def solution(arr):
    stack = []
    
    for i in range(len(arr)):
        if not stack:
            stack.append(arr[i])
        elif stack and stack[-1] == arr[i]:
            stack.pop()
        elif stack and stack[-1] != arr[i]:
            stack.append(arr[i])
    
    if not stack:
        return [-1]
    else:
        return stack
