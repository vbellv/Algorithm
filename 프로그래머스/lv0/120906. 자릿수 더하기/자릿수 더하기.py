def solution(n):
    num_list = []
    while n >= 1:
        num = n % 10
        num_list.append(num)
        n = n // 10
    return sum(num_list)