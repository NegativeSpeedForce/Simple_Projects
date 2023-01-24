def squaring_numbers(numbers):
    squared_numbers = []
    for i in numbers:
        squared_number = i ** 2
        squared_numbers.append(squared_number)
    return squared_numbers


star = [1,2,3,4,5,6,7,8,9]

print(squaring_numbers(star))
