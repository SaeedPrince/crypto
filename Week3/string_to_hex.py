conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
def decTohex(n):
    if(n<=0):
        hexa = ''
    else:
        remainder = n%16
        hexa = decTohex(n//16)+conversion_table[remainder]
    return  hexa
        
def str_to_hex(input_string):
    for character in input_string:
        ascii_code = ord(character)
        result = decTohex(ascii_code)
        print(f'0x{result} ', end='')
    print('')

if __name__ == '__main__':
    str_to_hex('hello')  # This should print the line '0x68 0x65 0x6c 0x6c 0x6f'

