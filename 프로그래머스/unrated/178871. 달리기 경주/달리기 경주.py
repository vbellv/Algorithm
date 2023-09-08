def solution(players, callings):
    # 처음 선수들의 순위를 딕셔너리에 저장
    play_dict = {}
    
    for idx, val in enumerate(players):
        play_dict[val] = idx
        
    for name in callings:
        # 이름이 호명된 선수의 현재 순위
        current_rank = play_dict[name]
        
        # 이름이 호명된 선수의 등수 높여주기
        # 이름이 호명된 선수의 앞에 있는 선수 등수 낮춰주기
        play_dict[name] -= 1
        play_dict[players[current_rank-1]] += 1
        
        # players 배열 바꿔주기
        # 호명된 선수의 앞에 있는 선수와 호명된 선수의 순서 바꾸기
        players[current_rank-1], players[current_rank] = name, players[current_rank-1]
        
    return players