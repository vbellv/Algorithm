word = str(input())
alphabet_dict = {}

for i in range(97, 123):
    alphabet_dict[chr(i)] = -1

for num in range(len(word)):
    alphabet_dict[word[num]] = word.index(word[num])

print(*list(alphabet_dict.values()))