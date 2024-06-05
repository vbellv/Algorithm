def solution(s):
    count = 0
    
    for index in range(len(s)):
        check_words = s[index:] + s[:index]
        
        stack = []
        for idx in range(len(check_words)):
            if not stack:
                stack.append(check_words[idx])
            else:
                if (stack[-1] == '[' and check_words[idx] == ']') or \
                    (stack[-1] == '{' and check_words[idx] == '}') or \
                    (stack[-1] == '(' and check_words[idx] == ')'):
                    stack.pop()
                else:
                    stack.append(check_words[idx])
        
        if not stack:
            count += 1
    
    return count
