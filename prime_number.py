"""
1. Write a program that finds all prime numbers up to n for input n.

Example output:

20 --> 2 3 5 7 11 13 17 19
"""


def prime_numbers(n):
    for i in range(2, n + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(i, end=" ")


n = int(input("Please enter a number: "))
prime_numbers(n)
