n = int(input())
num_list = list(map(int, input().split()))
v = int(input())

cnt_v = [num for num in num_list if v == num]        
print(len(cnt_v))