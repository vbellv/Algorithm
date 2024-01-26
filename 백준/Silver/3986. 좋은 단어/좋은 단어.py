n = int(input())
words = [list(map(str, input().rstrip())) for _ in range(n)]
cnt = 0

for i in range(n):
    stack = []
    for word in words[i]:
        if not stack:
            stack.append(word)
        else:
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
    if not stack:
        cnt += 1

print(cnt)