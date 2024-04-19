def calculate_distance(numbers_dict, hand, number, distance):
    hand_distance = 0
    hand_distance += distance[numbers_dict[hand]][numbers_dict[number]]

    return hand_distance

def solution(numbers, hand):
    numbers_dict = {1: 0, 2: 0, 3: 0, 
                    4: 1, 5: 1, 6: 1,
                    7: 2, 8: 2, 9: 2,
                    10: 3, 0: 3, 11: 3}
    answer = ''
    left_hand, right_hand = 10, 11
    
    edge_keypad_distance = [[1, 2, 3, 4], [2, 1, 2, 3], [3, 2, 1, 2], [4, 3, 2, 1]]
    median_keypad_distance = [[0, 1, 2, 3], [1, 0, 1, 2], [2, 1, 0, 1], [3, 2, 1, 0]]
    
    for number in numbers:
        if number in [1, 4, 7, 10]:
            answer += 'L'
            left_hand = number
        elif number in [3, 6, 9, 11]:
            answer += 'R'
            right_hand = number
        else:
            # print('num', number, 'left', left_hand, 'right', right_hand)
            left_distance, right_distance = 0, 0
            
            if left_hand in [1, 4, 7, 10] and right_hand in [3, 6, 9, 11]:
                left_distance = calculate_distance(numbers_dict, left_hand, number, edge_keypad_distance)
                right_distance = calculate_distance(numbers_dict, right_hand, number, edge_keypad_distance)
                
                # print('1', left_distance, right_distance)
                
            elif left_hand in [2, 5, 8, 0] and right_hand in [3, 6, 9, 11]:
                left_distance = calculate_distance(numbers_dict, left_hand, number, median_keypad_distance)
                right_distance = calculate_distance(numbers_dict, right_hand, number, edge_keypad_distance)
                
                # print('2', left_distance, right_distance)
                
            elif left_hand in [1, 4, 7, 10] and right_hand in [2, 5, 8, 0]:
                left_distance = calculate_distance(numbers_dict, left_hand, number, edge_keypad_distance)
                right_distance = calculate_distance(numbers_dict, right_hand, number, median_keypad_distance)
                
                # print('3', left_distance, right_distance)
                
            elif left_hand in [2, 5, 8, 0] and right_hand in [2, 5, 8, 0]:
                left_distance = calculate_distance(numbers_dict, left_hand, number, median_keypad_distance)
                right_distance = calculate_distance(numbers_dict, right_hand, number, median_keypad_distance)
                
                # print('4', left_distance, right_distance)
            
            if left_distance > right_distance:
                answer += 'R'
                right_hand = number
            elif left_distance < right_distance:
                answer += 'L'
                left_hand = number
            else:
                if hand == 'right':
                    answer += 'R'
                    right_hand = number
                else:
                    if hand == 'left':
                        answer += 'L'
                        left_hand = number
                        
            # print('ans', answer)
            # print('==============')
            # print()
    return answer
            
            