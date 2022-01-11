#!/url/bin/python  #Это строка для работы в Linux

# Импортирую библиотеку sys для работы с CLI

import sys
import mmap

# Поиск system.applicationHost
def check():
    with open('C:\\Users\\alexandr.kozlov\\Desktop\\applicationHost.config') as f:
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# s.find ведет себя как  Bytearray поэтому необходимо добавить b
        if s.find(b"<system.applicationHost>") != -1:
            print('true')
        else:
            print('false')


check()
