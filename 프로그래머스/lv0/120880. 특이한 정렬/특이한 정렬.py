def solution(numlist, n):
    num_list = sorted([(abs(num-n), num) for num in numlist], key=lambda x : x[0])

    for i in range(len(num_list)-1):
        if (num_list[i][0] == num_list[i+1][0]) and (num_list[i][1] < num_list[i+1][1]):
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            
    return [num[1] for num in num_list]