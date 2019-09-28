from math import inf


def square_number(number):
    """f(x) = x^2"""
    return number*number


def get_smallest_number(numbers):
    smallest_number = inf

    for number in numbers:
        if number < smallest_number:
            smallest_number = number

    return smallest_number


def get_largest_number(numbers):
    largest_number = -inf

    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number


def get_divisible_by_5_(numbers):
    for number in numbers:
        if number % 5 == 0:
            yield number


def get_divisible_by(numbers, divisor):
    numbers_divisible_by = []
    for number in numbers:
        if number % divisor == 0:
            numbers_divisible_by.append(number)

    return numbers_divisible_by


def get_divisible_by_5(numbers):
    return get_divisible_by(numbers, 5)


print(get_divisible_by(range(1, 101), 3))

# 1 1 2 3 5 8 13 21


def get_fib_number(n):
    if n == 1 or n == 2:
        return 1

    fib_prev = 1
    fib_preprev = 1

    for _ in range(3, n+1):
        fib_number = fib_prev + fib_preprev
        fib_prev, fib_preprev = fib_number, fib_prev

    return fib_number


print(get_fib_number(30))
