def solution(s):
    word_all_index, word_index_list = [], []
    
    # 중복되는 단어에 대한 모든 인덱스 저장
    for word in set(s):
        word_all_index.append((word, list(filter(lambda x: s[x] == word, range(len(s))))))
    
    # index의 길이가 1이면 -1 저장, 1을 초과하면 index를 순회하며 1의 위치만큼 차이값을 저장
    for word, index in word_all_index:
        if len(index) == 1:
            for num in range(len(index)):
                word_index_list.append((word, -1, index[num]))
        else:
            for num in range(len(index)):
                if num == 0:
                    word_index_list.append((word, -1, index[num]))
                elif num > 0:
                    word_index_list.append((word, index[num] - index[num-1], index[num]))
    
    # 원래 단어에 해당하는 인덱스 순서대로 정렬
    word_index_list = sorted(word_index_list, key=lambda x: x[2])
    
    # 구하려는 글자 위치값 반환
    return [num for _, num, _ in word_index_list]