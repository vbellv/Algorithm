n, m = map(int, input().split())

def euclidean_algorithm(num1, num2):
    left = num2
    right = num1 % num2
    return left, right

num1, num2 = max(n, m), min(n, m)
left, right = euclidean_algorithm(num1, num2)
    
while True:
    if right == 0:
        break
    left, right = euclidean_algorithm(left, right)
    
greatest_common = left
least_common = left * (n//left) * (m//left)

print(greatest_common)
print(least_common)