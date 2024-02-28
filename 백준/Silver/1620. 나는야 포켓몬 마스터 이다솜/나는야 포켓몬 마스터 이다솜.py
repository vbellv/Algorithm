import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon_number, pokemon_name = {}, {}

for i in range(1, n+1):
    name = str(input().rstrip())
    pokemon_name[name] = i
    pokemon_number[i] = name

for i in range(1, m+1):
    quiz = str(input().rstrip())

    if quiz.isdigit():
        print(pokemon_number[int(quiz)])
    else:
        print(pokemon_name[quiz])