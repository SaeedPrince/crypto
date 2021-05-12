from helper_functions import binary
def bitwise_or(integer_a, integer_b):
    print(f'The bitwise OR of {binary(integer_a)} and {binary(integer_b)} is: ')
    result = integer_a | integer_b
    print(f'Result: {binary(result)}')
    return result

if __name__ == '__main__':
    bitwise_or(85, 170)
