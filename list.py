#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: November 2019
# This program goes to a certain decimal place

import math


def calculation(numbers):
    # calculates numbers
    added_number = numbers[0] + numbers[1]
    numbers.append(added_number)
    subtracted_number = numbers[0] - numbers[1]
    numbers.append(subtracted_number)
    multiplied_number = numbers[0] * numbers[1]
    numbers.append(multiplied_number)

    return numbers


def main():
    # calls other functions and get inputs
    numbers = []

    while True:
        first_number_string = input("Input a number: ")
        second_number_string = input("Input another number: ")

        try:
            first_number = int(first_number_string)
            second_number = int(second_number_string)

            numbers.append(first_number)
            numbers.append(second_number)

            calculation(numbers)

            print("{0} + {1} = {2}".format(numbers[0], numbers[1], numbers[2]))
            print("{0} - {1} = {2}".format(numbers[0], numbers[1], numbers[3]))
            print("{0} x {1} = {2}".format(numbers[0], numbers[1], numbers[4]))
            break

        except(ValueError):
            print("Not a valid number inputted")
            print("")


if __name__ == "__main__":
    main()
