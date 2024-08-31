#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, length):
            next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
            fibonacci_sequence.append(next_number)
        print(fibonacci_sequence)