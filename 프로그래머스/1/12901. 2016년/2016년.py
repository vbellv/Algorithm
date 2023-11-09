def solution(a, b):
    calendar_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    day_list = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    days = (sum(calendar_dict[num] for num in range(1, a)) + b) % 7 - 1
    
    return day_list[days]