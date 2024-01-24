def solution(s):
    stack = []
    
    for word in s:
        if not stack:
            stack.append(word)
        else:
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
    
    if not stack:
        return 1
    else:
        return 0 