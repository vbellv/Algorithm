def solution(numbers, direction):
    return [numbers[-i+(len(numbers)-1)] if direction == 'right' else numbers[-i+1] for i in range(len(numbers), 0, -1)]