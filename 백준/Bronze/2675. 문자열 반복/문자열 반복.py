n = int(input())

for i in range(n):
    num, words = map(str, input().split())
    answer = ''
    for word in words:
        answer += word * int(num)
    print(answer)