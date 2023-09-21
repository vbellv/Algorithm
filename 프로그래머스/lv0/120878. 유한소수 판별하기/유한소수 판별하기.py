def solution(a, b):
    print(a/b, round(a/b, 4))
    return 1 if a/b == round(a/b, 10) else 2

print(solution(1, 16))
print(solution(1, 1024))