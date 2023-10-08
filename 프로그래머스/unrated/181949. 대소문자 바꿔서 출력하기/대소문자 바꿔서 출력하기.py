str = map(str, input().strip())
word_list = ''
for word in str:
    if word == word.lower():
        word_list += word.upper()
    else:
        word_list += word.lower()
        
print(word_list)