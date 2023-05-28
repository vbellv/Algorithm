import sys
from collections import defaultdict
input = sys.stdin.readline

words = list(map(str, input().rstrip()))
alphabet = list(map(chr, range(97, 123)))
num_dict = defaultdict(list)

for num in range(2, 10):
    num_dict[num]

num = 2
while num < 10:
    for idx, val in enumerate(alphabet):
        if num <= 6:
            if idx // 3 == (num-2):
                num_dict[num] += [val.upper()]
        elif num == 7:
            if idx >= (num*2)+1 and idx < (num*2)+5:
                num_dict[num] += [val.upper()]
        elif num == 8:
            if idx >= (num*2)+3 and idx < (num*2)+6:
                num_dict[num] += [val.upper()]
        else:
            if idx >= (num*2)+4 and idx < (num*2)+8:
                num_dict[num] += [val.upper()]       
    num += 1

time = 0
for key, value in num_dict.items():
    for word in words:
        if word in value:
            time += key + 1
print(time)