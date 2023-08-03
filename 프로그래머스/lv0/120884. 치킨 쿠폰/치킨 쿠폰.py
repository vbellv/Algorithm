def solution(chicken):
    # 총 chicken의 수 = 총 쿠폰 개수
    service_chicken = 0  # 서비스 치킨 수
    extra_coupon = 0     # 남은 쿠폰 수
    
    while chicken >= 10:
        # 서비스 치킨 개수 = 총 쿠폰 개수 // 10장
        service_chicken += chicken // 10
        # 남은 쿠폰 수 = 총 쿠폰 개수 % 10장
        extra_coupon += chicken % 10
        chicken = chicken // 10
    
        # 남은 총 쿠폰(chicken)이 1인 경우,
        # 서비스 치킨 1마리를 먹었다는 의미 == 쿠폰 1장이 생겼다는 의미
        if chicken < 10:
            extra_coupon += chicken
    
    
    # 쿠폰들의 총합이 10개가 넘을 경우,
    # 쿠폰 10장당 서비스 치킨 1마리를 먹을 수 있기 때문에 10으로 나눠줌
    # 단, 쿠폰 10장을 쓰고 남은 총 쿠폰 수에 서비스 치킨으로 받은 쿠폰 개수를 추가로 더해줌
    while extra_coupon >= 10:
        service_chicken += extra_coupon // 10
        extra_coupon = extra_coupon // 10 + extra_coupon % 10
        
    return service_chicken