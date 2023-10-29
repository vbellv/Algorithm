def user_dictionary(id_list, report):
    report_dict, user_dict = {}, {}
    
    for id in id_list:
        report_dict[id] = 0
        user_dict[id] = 0
    
    for names in set(report):
        report_dict[names.split(' ')[1]] += 1
        
    return report_dict, user_dict


def solution(id_list, report, k):
    report_dict, user_dict = user_dictionary(id_list, report)
    
    report_user = [key for key, val in report_dict.items() if val >= k]
    cnt = 0
    
    for names in set(report):
        if names.split(' ')[1] in report_user:
            user_dict[names.split(' ')[0]] += 1
            
    return list(user_dict.values())