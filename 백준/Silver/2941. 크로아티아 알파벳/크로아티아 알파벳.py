alphabet = str(input())

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

for word in croatia:
    if word in alphabet:
        if alphabet.count(word) > 1:
            cnt += alphabet.count(word)
        else:
            cnt += 1
        alphabet = alphabet.replace(word, ' ')

alphabet = alphabet.replace(' ', '')
print(cnt + len(alphabet))