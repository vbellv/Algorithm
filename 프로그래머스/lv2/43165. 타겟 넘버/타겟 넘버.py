def solution(numbers, target):
    
    def dfs(idx, current_sum):
        # nonlocal : 중첩함수 내에서 비지역변수를 대상으로 사용
        # 변수 앞에 nonlocal 키워드를 붙여주면 중첩 함수 내에서 값을 변경하더라도 새로운 지역 변수가 되지 않고 함수 밖에서 이미 선언된 비전역 변수를 가리키게 됨
        nonlocal count
        # 현재 인덱스 값과 numbers 배열의 길이와 같은지 확인
        # 같다면 모든 숫자를 처리한 것
        if idx == len(numbers):
            # 현재까지의 합과 target 값이 같다면 count를 1 증가시켜줌
            if current_sum == target:
                count += 1
            return
        
        # dfs 알고리즘을 재귀적으로 사용
        # 현재 인덱스를 1씩 증가시켜주면서 현재까지의 합에서 numbers 배열의 해당 인덱스를 더하거나 감소시킴
        dfs(idx + 1, current_sum + numbers[idx])
        dfs(idx + 1, current_sum - numbers[idx])
    
    # count를 0으로 초기화해주고, dfs() 함수도 시작 인덱스를 0으로, 현재까지의 합을 0으로 초기화해줌
    count = 0
    dfs(0, 0)
    
    return count