word_list = [list(map(str, input().rstrip())) for _ in range(5)]
temp_word = [len(word_list[i]) for i in range(len(word_list))]
    
for i in range(len(word_list)):
    while True:
        if len(word_list[i]) < max(temp_word):
            word_list[i].append('')
        elif len(word_list[i]) == max(temp_word):
            break

idx = 0
while idx < max(temp_word):
    for i in range(5):
        print(word_list[i][idx], end='')
    idx += 1