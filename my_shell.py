import os

__author__ = "Roi Carmona"
SHELL_NAME = "Epsilon Shell"
START_PATH = os.path.expanduser('~').split('\\')
USERS_NAME = os.getlogin()
SHELL_VER  = '1.0' 

from commands import *
import protocol

def main():
    global START_PATH

    while True:
        path_to_show = protocol.show_path(START_PATH)

        user_req = input(f"{USERS_NAME}: {path_to_show}> ")

        try:
            #splitted = shlex.split(user_req, posix=True)
            splitted = protocol.split_command(user_req)
        except:
            print('Something is wrong with your request')
            continue

        command = splitted[0].lower()

        if command == "help":
            CMD_Commands.help()

        elif command == "hello":
            if len(splitted) == 1:
                CMD_Commands.hello()
            elif len(splitted) == 3 and ">" in splitted:
                CMD_Commands.hello(splitted[2])
            else:
                print('Something is wrong')

        elif command == "hexdump":
            if len(splitted) == 2:
                protocol.run_with_popen(command, splitted[1])
            elif len(splitted) == 4 and (splitted[2] == ">"):
                protocol.run_with_popen(command, splitted[1], splitted[3])
            elif len(splitted) == 5 and splitted[2] == "|":
                protocol.pipe(splitted[1], splitted[4])
            else:
                print('Something is wrong with the command you entered')

        elif command == "grep":
            try:
                if len(splitted) == 2:
                    protocol.run_with_popen(command, splitted[1])
                elif len(splitted) == 3:
                    protocol.run_with_popen(command, splitted[1], splitted[2])
                else:
                    print('''Examples: hexdump "myfile.exe" | grep "ff"
          grep "ff" "path_to_myfile"''')
            except:
                print('Something is wrong')
        elif command == "ls":
            try:
                CMD_Commands.ls(splitted[1])
            except:
                CMD_Commands.ls('')
        
        elif command == "pwd":
            CMD_Commands.pwd()
        
        elif command == "cd":
            try:
                START_PATH = CMD_Commands.cd(splitted[1])
            except:
                print('Please supply a path')

        elif command == "cls":
            CMD_Commands.cls()

        elif command == "exec":
            try:
                CMD_Commands.exec(splitted[1])
            except:
                print('Please supply a file')
        
        elif command == "ren":
            try:
                CMD_Commands.ren(splitted[1], splitted[2])
            except:
                print("Please supply both paths")
        
        elif command == "cp":
            try:
                CMD_Commands.cp(splitted[1], splitted[2])
            except:
                print("Please supply both paths")
        
        elif command == "rm":
            try:
                CMD_Commands.rm(splitted[1])
            except:
                print("Please supply a file to remove")

        elif command == "zen":
            CMD_Commands.zen()

        elif command == "set":
            if len(splitted) == 1:
                CMD_Commands.print_set_list('')
            elif '=' not in "".join(splitted[1:]):
                CMD_Commands.print_set_list(splitted[1])
            else:
                CMD_Commands.change_set_value("".join(splitted[1:]).split('='))

        elif command == "exit":
            break
        
        else:
            print("The command entred is unknown... type: 'help' to view the commands")


if __name__ == "__main__":
    protocol.hello_message()
    main()
