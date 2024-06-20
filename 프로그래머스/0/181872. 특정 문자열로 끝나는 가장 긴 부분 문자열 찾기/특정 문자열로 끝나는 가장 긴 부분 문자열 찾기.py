def solution(myString, pat):
    stack = []
    myString = list(myString)
    
    while True:
        word = myString.pop()
        stack.append(word)

        try:
            if stack[-len(pat):][::-1] == list(pat):
                return ''.join(myString) + pat
        except:
            pass
