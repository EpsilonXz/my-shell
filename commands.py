import os
import json
import glob
import protocol
from my_shell import START_PATH, USERS_NAME
import shutil
import set_list

class CMD_Commands:
    def help():
        print()
        with open('cmds_help.json', 'r') as f:
            data = json.load(f)

            for i in data['Commands']:
                print(i["CMD_NAME"] + " : " + i["CMD_HELP"])
        print()


    def hello(path = ''):
        to_say = f'Hello {USERS_NAME}\n'
        print(to_say)

        if path != '':
            protocol.side_pattern_to_file(path, to_say)


    def ls(path):
        try:
            path = protocol.check_path_for_ls(path)

            if path == 'Unknown':
                raise Exception

            names = map(os.path.basename, glob.glob(f"{path}\\*"))

            for name in names:
                print(name.replace('\\', ''))
        except Exception:
            print('The directory doesnt exist')
    

    def pwd():
        print(protocol.show_path(START_PATH))
    

    def cd(path_given):
        global START_PATH
        
        as_path = "\\".join(START_PATH)

        try:
            if os.path.exists(path_given) and os.path.isabs(path_given):
                to_path = path_given
                START_PATH = to_path.split('\\')
                protocol.START_PATH = START_PATH
            elif not os.path.exists(as_path + "\\" + path_given):
                raise Exception
            else:
                START_PATH.append(path_given)
                START_PATH = protocol.get_good_path(START_PATH)
                to_path = "\\".join(START_PATH)
            
            return START_PATH
        except Exception:
            print("The directory doesnt exist")
            return START_PATH

    def cls():
        os.system('cls')
    

    def exec(path):
        full_path = protocol.search_file(path)

        if full_path == 'Unknown':
            print('The file doesnt exist')
        else:
            os.startfile(full_path)
    
    def ren(old, new):
        old_path = protocol.check_path(old)
        new_path = protocol.check_path(new)

        if old_path == 'Unknown' or new_path == "Unknown":
            print('One of the paths is wrong')
        else:
            os.rename(old_path, new_path)
    

    def cp(old, new):
        old_path = protocol.check_path(old)
        new_path = protocol.check_path(new)

        if old_path == 'Unknown' or new_path == "Unknown":
            print('One of the paths is wrong')
        else:
            shutil.copy2(old_path, new_path)
    

    def rm(path):
        new_path = protocol.check_path(path)

        if new_path == 'Unknown':
            print('The file doesnt exist')
        else:
            os.remove(new_path)
    

    def zen():
        s = """Gur Mra bs Clguba, ol Gvz Crgref

        Ornhgvshy vf orggre guna htyl.
        Rkcyvpvg vf orggre guna vzcyvpvg.
        Fvzcyr vf orggre guna pbzcyrk.
        Pbzcyrk vf orggre guna pbzcyvpngrq.
        Syng vf orggre guna arfgrq.
        Fcnefr vf orggre guna qrafr.
        Ernqnovyvgl pbhagf.
        Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
        Nygubhtu cenpgvpnyvgl orngf chevgl.
        Reebef fubhyq arire cnff fvyragyl.
        Hayrff rkcyvpvgyl fvyraprq.
        Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
        Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
        Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
        Abj vf orggre guna arire.
        Nygubhtu arire vf bsgra orggre guna *evtug* abj.
        Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
        Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
        Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

        d = {}
        for c in (65, 97):
            for i in range(26):
                d[chr(i+c)] = chr((i+13) % 26 + c)

        print("".join([d.get(c, c) for c in s]))


    def print_set_list(in_got):
        if in_got == '':
            for key in set_list.SL:
                print(f'{key} = {set_list.SL[key]}')
        else:
            for key in set_list.SL:
                if key.startswith(in_got):
                   print(f'{key} = {set_list.SL[key]}')
    
    def change_set_value(to_change):
        key, value = to_change

        set_list.SL[key] = value
