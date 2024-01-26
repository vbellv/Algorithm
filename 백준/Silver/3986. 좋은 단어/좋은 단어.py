n = int(input())
words = [list(map(str, input().rstrip())) for _ in range(n)]
cnt = 0

for i in range(n):
    stack = []
    for j in range(len(words[i])):
        if not stack:
            stack.append(words[i].pop())
        else:
            word = words[i].pop()
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
    if not stack:
        cnt += 1
    else:
        continue

print(cnt)