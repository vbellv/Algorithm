num = int(input())

for _ in range(num):
    word = str(input().strip())
    print(word[0]+word[-1])