numbers = [int(input()) for _ in range(3)]
multiply_numbers = str(numbers[0] * numbers[1] * numbers[2])

for i in range(0, 10):
    print(multiply_numbers.count(str(i)))