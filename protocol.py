import os
from my_shell import START_PATH, SHELL_NAME, USERS_NAME
from subprocess import *

def hello_message():
    print()
    print(f'Hello {USERS_NAME}, welcome to {SHELL_NAME}.')
    print()


def split_command(cmd):
    splitted = cmd.split(' ')
    
    only_correct = [word for word in splitted if word != ""]

    return only_correct

def check_path_for_ls(path):
    global START_PATH

    current_path = '\\'.join(START_PATH)
    if path == '' or path == '.':
        path = current_path
    elif os.path.isabs(path) and os.path.exists(path):
        pass
    else:
        path = current_path + '\\' + path
        if os.path.exists(path):
            return path
        else:
            return 'Unknown'
    
    return path

def get_good_path(path_arr):
    global START_PATH

    second_path = "\\".join(path_arr)
    second_path = second_path.replace('/', '\\')
    splitted_path = second_path.split('\\')
    count = 0
    for part in splitted_path:
        if part == '..': count += 1

    right_path2 = [part for part in splitted_path if part != '..' and part != '' and part != '.']

    if count != 0:
        for i in range(count):
            if len(right_path2) > 1:
                right_path2.pop()
            else:
                print("You cannot go any further")

    if len(right_path2) == 1:
        from set_list import SL
        START_PATH = [SL['HOMEDRIVE']]
        print(START_PATH)
    else:
        START_PATH = right_path2
    return right_path2


def show_path(path_arr):
    return "\\".join(path_arr)


def check_path(path_g):
    global START_PATH

    print(path_g)
    path_g = path_g.replace('/', '\\')

    if os.path.isabs(path_g) and os.path.exists(path_g):
        return path_g
    
    new_path = "\\".join(START_PATH) + "\\" + path_g
    
    if os.path.isabs(new_path) and os.path.exists(new_path):
        return new_path
    
    else:
        return 'Unknown'


def search_file(path_given):
    path_given = path_given.replace('/', '\\')
    if os.path.isfile(path_given):
        return path_given

    global START_PATH
    from set_list import SL

    splitted_path = SL['Path'].split(';')
    path_comb = "\\".join(START_PATH) + "\\" + path_given

    if os.path.isfile(path_comb):
        return path_comb

    for path in splitted_path:
        path_comb = path + "\\" + path_given

        if os.path.isfile(path_comb):
            return path_comb
    
    return 'Unknown'


def check_non_exist_file(path):
    global START_PATH

    start_p = "\\".join(START_PATH)
    splitted = path.split('\\')
    
    if len(splitted) == 1:
        return start_p + "\\" + path
    
    route = splitted[:-1:]
    dir_to_file = "\\".join(route)

    if os.path.exists(dir_to_file) and os.path.isdir(dir_to_file):
        return path
    
    elif os.path.exists(start_p + "\\" + dir_to_file) and os.path.isdir(start_p + "\\" + dir_to_file):
        return start_p + "\\" + path
    
    else:
        return 'Unknown'


def side_pattern_to_file(path2, to_write):
    full_path2 = check_non_exist_file(path2)

    if full_path2 == "Unknown":
        print('There was a problem with the second path')
        return
    if full_path2.endswith('.txt'):
        f = open(full_path2, 'w')
    else:
        to_open = full_path2 + '.txt'
        f = open(to_open, 'w')
    try:
        f.write(to_write)
        print('Successfully written to file')
    except:
        print('There was a problem writing to the file')
    f.close()

def pipe(argument1, argument2):
    p1 = Popen(["python", "hexdump.py", argument1], stdout=PIPE, shell=None)
    p2 = Popen(["python", "grep.py", argument2], stdin=p1.stdout, shell=None)
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.

    output = p2.communicate()[0]

    if output:
        print(output)

def run_with_popen(command, argument1, argument2=''):
    p = Popen(["python", f"{command}.py", argument1, argument2],stdout=PIPE, shell=None, text=True)
    output = p.communicate()[0]
    
    if output:
        print(output)
