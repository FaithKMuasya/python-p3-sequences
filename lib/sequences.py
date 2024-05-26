#!/usr/bin/env python3

def print_fibonacci(length):

    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    my_fib_sequence = [0, 1]
    for _ in range(2, length):
        my_fib_sequence.append(my_fib_sequence[-1] + my_fib_sequence[-2])

    print(my_fib_sequence)



    pass