#!/url/bin/python  #Это строка для работы в Linux

# Импортирую библиотеку sys для работы с CLI

import mmap

# Словарь для записи информации
data = {}

# Поиск system.applicationHost

def check():
    with open('C:\\Users\\alexandr.kozlov\\Desktop\\applicationHost.config') as f:
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# s.find ведет себя как  Bytearray поэтому необходимо добавить b
        if s.find(b"<system.applicationHost>") != -1:
            print('true')
        else:
            print('false')

def information():
    answer = 'yes'
    while answer == 'yes':
        if answer == 'yes':
            print("Вы хотите создать Web или Win сервис?(web/win) ")
            serv = input()
            if serv == "web":
                print("Введите наименование Web сервиса: ")
                Nameweb = input()
                print("\nВведите имя учетной записи: ")
                Nameuser = input()
                print("\nВведите пароль от учетной записи: ")
                password = input()
                print("\n Хотите ли добавить еще application Pool?(yes/no) ")
                answer = input()
                data[Nameweb] = [Nameuser, password, "web"]
            else:
                print("Введите наименование Win сервиса: ")
                Namewin = input()
                print("\nВведите имя учетной записи: ")
                Nameuser = input()
                print("\nВведите пароль от учетной записи: ")
                password = input()
                print("\n Хотите ли добавить еще application Pool?(yes/no) ")
                answer = input()
                data[Namewin] = [Nameuser, password, "win"]
    print(data)

information()
