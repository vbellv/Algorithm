def solution(n):
    binary_num = bin(n)[2:]
    count_one = str(binary_num).count('1')
    
    while True:
        n += 1
        binary_num = bin(n)[2:]
        new_count_one = str(binary_num).count('1')

        if new_count_one == count_one:
            return n