import sys
input = sys.stdin.readline

n, m = map(int, input().split())
names_1 = list(str(input().rstrip()) for _ in range(n))
check_dict = dict.fromkeys(names_1, 0)
answer = []

for _ in range(m):
    name = str(input().rstrip())
    try:
        check_dict[name] += 1
    except:
        pass

for key, value in check_dict.items():
    if value != 0:
        answer.append(key)

print(len(answer))
for name in sorted(answer):
    print(name)