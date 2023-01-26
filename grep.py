import os
import re
import sys

def read_from_string(arg):
    while True:
        try:
            line = input()

            if arg in line:
                print(line)
        except:
            break

def read_from_file(supply, path):
    from protocol import search_file

    full_path = search_file(path)
    if full_path == "Unknown":
        print("Something wrong with path given")
        sys.exit()
    
    try:
        file = open(full_path, 'rb')
    except:
        print('Something is wrong with the path given')
        file.close()
        raise Exception

    try:
        dec = file.readlines()

        for line in dec:
            if re.search(supply, str(line)):
                print(str(line) + "\n")
    except Exception as e: 
        print(e)
        file.close()


try:
    try:
        supply = sys.argv[1]
    except:
        raise Exception

    if len(sys.argv) == 2:
        read_from_string(supply)

    elif len(sys.argv) == 3:
        try:
            path = sys.argv[2]
        except:
            raise Exception

        read_from_file(supply, path)

except Exception:
    print('''Examples: hexdump "myfile.exe" | grep "ff"
          grep "ff" "path_to_myfile"''')
