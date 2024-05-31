import math


def is_perfect_number(number):
    for i in range(2, number):
        divisors_sum = sum([divisor for divisor in range(1, number) if number % divisor == 0])
        return divisors_sum == number


def perfect_numbers_in_range(limit):
    perfect_numbers = [num for num in range(2, limit) if is_perfect_number(num)]
    return perfect_numbers


#Example usage:
input_number = int(input("enter a number: "))

print(perfect_numbers_in_range(input_number))
