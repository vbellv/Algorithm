def solution(a, d, included):
    n = len(included)
    ad_list = [num for num in range(a, d*n+a, d)]
    ad_included_sum = 0
    
    for idx in range(len(included)):
        if included[idx] == True:
            ad_included_sum += ad_list[idx]
            
    return ad_included_sum