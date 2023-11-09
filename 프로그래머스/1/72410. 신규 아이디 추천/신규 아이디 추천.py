import re

def recommend_id(new_id):
    except_words = '[a-z0-9\-\_\.]'
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    new_id = ''.join(re.findall(except_words, new_id))

    # 3단계
    new_id = re.sub('\.+', '.', new_id)
    
    # 4단계
    if new_id.startswith("."):
        new_id = new_id[1:]
    
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    
    # 5단계
    if new_id == "":
        new_id += 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
    
    # 7단계
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3-len(new_id))
        
    return new_id

def solution(new_id):
    return recommend_id(new_id)