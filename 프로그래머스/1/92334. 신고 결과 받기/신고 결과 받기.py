from collections import Counter

def solution(id_list, report, k):
    reports = Counter([names.split(' ')[1] for names in set(report)])
    suspended_users = [name for name, cnt in reports.items() if cnt >= k]
    
    send_emails = dict.fromkeys(id_list, 0)
    
    for names in set(report):
        if names.split(' ')[1] in suspended_users:
            send_emails[names.split(' ')[0]] += 1
            
    return list(send_emails.values())