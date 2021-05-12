conversion_table = ['0', '1']
def decTobin(n):
    if(n<=0):
        bina = ''
    else:
        remainder = n%2
        bina = decTobin(n//2)+conversion_table[remainder]
    return  bina

def str_to_binary(input_string):
    for character in input_string:
        ascii_code = ord(character)
        result = decTobin(ascii_code)
        print(f'0b{result} ', end='')
    print('')




if __name__ == '__main__':
    str_to_binary('hello')  # Should print the line: 0b1101000 0b1100101 0b1101100 0b1101100 0b1101111
