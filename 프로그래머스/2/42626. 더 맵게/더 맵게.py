import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        if scoville[0] >= K:
            break
        else:
            first_min_num = heapq.heappop(scoville)
            second_min_num = heapq.heappop(scoville)

            new_scoville = first_min_num + second_min_num * 2
            heapq.heappush(scoville, new_scoville)

            cnt += 1
            
    if scoville[0] < K:
        return -1
    else:
        return cnt