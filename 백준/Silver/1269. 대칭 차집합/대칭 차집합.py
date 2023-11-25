n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(len(set(A)-set(B))+len(set(B)-set(A)))