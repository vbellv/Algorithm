import sys
input = sys.stdin.readline

people = list(int(input()) for _ in range(9))
not_one, not_two = 0, 0

for i in range(len(people)):
    for j in range(i+1, len(people)):
        if sum(people) - people[i] - people[j] == 100:
            not_one = people[i]
            not_two = people[j]
            
people.remove(not_one)
people.remove(not_two)

for person in sorted(people):
    print(person)