from math import inf

# eigene Funktion impotieren
from test import frage_passwort


def square_number(number):
    """f(x) = x^2 (x hoch 2)"""
    return number * number


# Aufgabe 2a.2
def get_smallest_number(numbers):
    """a)"""
    smallest_number = inf
    for number in numbers:
        if number < smallest_number:
            smallest_number = number

    return smallest_number


def get_largest_number(numbers):
    """b)"""
    largest_number = -inf
    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number


def get_divisible_by(numbers, divisor):
    """d)"""
    numbers_divisible_by = []
    for number in numbers:
        if number % divisor == 0:
            numbers_divisible_by.append(number)

    return numbers_divisible_by


def get_divisible_by_5(numbers):
    """ d) mit Hilfe von c)"""
    return get_divisible_by(numbers, 5)
