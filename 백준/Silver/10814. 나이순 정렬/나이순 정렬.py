n = int(input())
members = []

for num in range(n):
    age, name = map(str, input().split())
    members.append((num, int(age), name))
    
for _, age, name in sorted(members, key=lambda x: (x[1], x[0])):
    print(age, name)