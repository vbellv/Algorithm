def solution(genres, plays):
    sum_dict = {}
    array = []
    answer = []

    # sum_dict : 장르별 누적합 딕셔너리 만들기
    for genre, play in zip(genres, plays):
        # get()를 사용할 시 처음에 key값에 genre가 없으면 0을 저장하고,
        # 그 다음에 장르별 재생횟수를 해당 key값에 해당하는 값을 더해줌
        sum_dict[genre] = sum_dict.get(genre, 0) + int(play)
    
    # 새로운 리스트에 value값으로 내림차순한 (key, value)을 저장
    sort_sum = sorted(sum_dict.items(), key=lambda x : x[1], reverse=True)
    
    # 인덱스별 장르와 재생횟수를 새로운 리스트에 저장
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        array.append([idx, genre, play])
    
    # 새로운 리스트에 앞선 리스트를 재생횟수 내림차순으로 정렬하여 저장
    sort_arr = sorted(array, key=lambda x : x[2], reverse=True)
    
    # 장르별 누적합 내림차순한 리스트를 순회하며
    for most_genre, _ in sort_sum:
        cnt = 0
        # 인덱스별 장르와 재생횟수 내림차순한 리스트를 순회하며
        for i in sort_arr:
            # 최대 2개씩 저장하기 위한 count
            if cnt == 2:
                break
            # 인덱스의 장르와 누적합 장르가 일치할 때
            if i[1] == most_genre:
                # 정답 리스트에 인덱스를 저장
                answer.append(i[0])
                # count를 하나씩 증가
                cnt += 1
                
    return answer