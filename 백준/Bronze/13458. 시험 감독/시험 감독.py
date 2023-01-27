import math

n = int(input())
data = list(map(int, input().split()))
b, c = map(int, input().split())

main_num = 0
sub_num = 0

for i in range(len(data)):
  if (data[i] - b) < 0 :
    main_num += 1
  else:
    main_num += 1
    sub_num = sub_num + math.ceil((data[i]-b)/c)

print(main_num + sub_num)