def solution(brown, yellow):
    for num in range(1, int(yellow ** 0.5) + 1):
        if yellow % num == 0:
            width, height = yellow // num, num
            
            if height * 2 + (width + 2) * 2 == brown:
                return [width + 2, height + 2]