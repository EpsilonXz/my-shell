
import re
import sys
import protocol
import binascii


def hexdump():
    print(sys.argv)
    try:
        path1 = sys.argv[1]
    except:
        raise Exception

    if len(sys.argv) == 3:
        path2 = sys.argv[2]
    else:
        path2 = ''
    
    print(path1, path2)

    bit_counter = 0
    row_number = 0
    full_dump = str(row_number).zfill(7) + " "
    try:
        full_path1 = protocol.search_file(path1)
        if full_path1 == 'Unknown':
            raise Exception

        with open(full_path1, 'rb') as f:
            content = f.read()
            dumped = str(binascii.hexlify(content))
            dumped = dumped[2:-1:]
            organized = ' '.join(re.findall('..', dumped))
            splitted = organized.split(' ')

            for bit in splitted:
                full_dump += bit + " "
                bit_counter += 1
                if bit_counter % 16 == 0:
                    full_dump += '\n'
                    row_number += 10
                    to_add = str(hex(bit_counter).split('x')[-1]).zfill(7) + " "
                    full_dump += to_add
            
            a = full_dump.split('\n')
            for line in a:
                print(line)
            
            # print(full_dump)

            if path2 != '':
                protocol.side_pattern_to_file(path2, full_dump)


    except Exception:
        try:
            if len(path1) > 1:
                print("The file was not found...")
            else:
                print('Please supply a path to the file after the command')
        except:
            print('Please supply a path to the file after the command')

if __name__ == "__main__":
    hexdump()