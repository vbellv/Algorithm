n = int(input())
words = sorted(list(set([str(input().rstrip()) for _ in range(n)])))

for word in sorted(words, key = lambda x: len(x)):
    print(word)