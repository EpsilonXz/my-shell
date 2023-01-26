import os
from my_shell import SHELL_NAME, SHELL_VER

SL = {'SHELL_NAME': SHELL_NAME,
      'COMPUTERNAME': os.getenv('COMPUTERNAME'),
      'SHELL_VER': SHELL_VER,
      'HOMEDRIVE': os.getenv('HOMEDRIVE'),
      'HOMEPATH': os.getenv('HOMEPATH'),
      'OS' : os.getenv('OS'),
      'SystemRoot': os.getenv('SystemRoot'),
      'Temp': os.getenv('Temp'),
      'USERNAME': os.getenv('USERNAME'),
      'USERPROFILE': os.getenv('USERPROFILE'),
      'PROCESSOR_ARCHITECTURE': os.getenv('PROCESSOR_ARCHITECTURE'),
      'PROCESSOR_IDENTIFIER': os.getenv('PROCESSOR_IDENTIFIER'),
      'PROCESSOR_LEVEL': os.getenv('PROCESSOR_LEVEL'),
      'NUMBER_OF_PROCESSORS': os.getenv('NUMBER_OF_PROCESSORS'),
      'Path': os.getenv('Path')
      

      }



