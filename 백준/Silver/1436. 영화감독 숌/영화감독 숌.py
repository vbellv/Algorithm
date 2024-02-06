n = int(input())
check_list = [0] * 10001
check = 1

for i in range(10000000):
    if '666' in str(i):
        check_list[check] = i
        check += 1
        
    if check == 10001:
        break
    
print(check_list[n])