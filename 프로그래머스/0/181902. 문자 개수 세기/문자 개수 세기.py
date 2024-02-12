import string

def alphabet_dictionary():
    alphabet_dict = {}
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    
    for word in alphabet:
        alphabet_dict[word] = 0
        
    return alphabet_dict    

def solution(my_string):
    answer = []
    alphabet_dict = alphabet_dictionary()
    
    for word in my_string:
        alphabet_dict[word] += 1
    
    for key, value in alphabet_dict.items():
        answer.append(value)
        
    return answer