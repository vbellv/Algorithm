import string

def solution(myString):
    alphabet = string.ascii_lowercase.split('l')
    
    for word in myString:
        if word in alphabet[0]:
            myString = myString.replace(word, 'l')
            
    return myString