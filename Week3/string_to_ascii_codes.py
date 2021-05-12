def str_to_ascii_codes(input_string):
    for character in input_string:
        ascii_code = ord(character)
        print(f'{ascii_code} ', end='')

if __name__ == '__main__':
    str_to_ascii_codes('hello')  # This should print the line '104 101 108 108 111'

