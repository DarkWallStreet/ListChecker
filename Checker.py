import os
from time import sleep

id = open('Config/ID.txt').readline()
univers = [univ for univ in os.listdir(r'lists/')]
if univers[0][-4:] =='.csv':
    univers = None
    names = [name for name in os.listdir(r'lists/')]
else:
    names = {}
    for univ in univers:
        names[univ] = [name for name in os.listdir(f'lists/{univ}/')]




if univers == None:
    for tb in names:
        # Порядковый номер, Приоритет конкурс, Подано согласие, Сумма баллов, Баллы за ВИ, Баллы за ИД, Статус, ID участника
        table = [line[0:-2].split(';')[0:-1] for line in open(f'lists/{tb}', encoding='utf-8').readlines()][1:]
        all_n = 0
        frst_n = 0
        for line in table:
            if line[-2] != '"Конкурсная группа исключена"':
                if line[-1] != id:
                    if line[1] == '1':
                        frst_n += 1
                    all_n += 1
                else:
                    # print(f'\033[1m{" ".join(tb[:-5].replace("_", " ").replace(".", " ").split()[:-2])}:')
                    # print(f'\033[0m\033[3mЛюдей выше Вас по рейтингу с приоритетом \033[1m1\033[0m : {frst_n}')
                    # print(f'\033[0m\033[3mЛюдей выше Вас по рейтингу \033[0m: {all_n}')
                    print(f'{" ".join(tb[:-5].replace("_", " ").replace(".", " ").split()[:-2])}:')
                    print(f'Людей выше Вас по рейтингу с приоритетом 1 : {frst_n}')
                    print(f'Людей выше Вас по рейтингу : {all_n}')

                    print('')
                    break
    sleep(999_999_999)

else:
    for univ in univers:
        # print(f'\033[1m------------------------------')
        # print(f'\033[0m   {univ}')
        # print(f'\033[1m------------------------------')
        print('------------------------------')
        print(f'   {univ}')
        print('------------------------------')

        print('')
        for tb in names[univ]:
            # Порядковый номер, Приоритет конкурс, Подано согласие, Сумма баллов, Баллы за ВИ, Баллы за ИД, Статус, ID участника
            table = [line[0:-2].split(';')[0:-1] for line in open(f'lists/{univ}/{tb}', encoding='utf-8').readlines()][1:]
            all_n = 0
            frst_n = 0
            for line in table:
                if line[-2] != '"Конкурсная группа исключена"':
                    if line[-1] != id:
                        if line[1] == '1':
                            frst_n += 1
                        all_n += 1
                    else:
                        # print(f'\033[1m {" ".join(tb[:-5].replace("_", " ").replace(".", " ").split()[:-2])}:')
                        # print(f'\033[0m\033[3m Людей выше Вас по рейтингу с приоритетом \033[1m1\033[0m : {frst_n}')
                        # print(f'\033[0m\033[3m Людей выше Вас по рейтингу \033[0m: {all_n}')
                        # print('')
                        print(f'{" ".join(tb[:-5].replace("_", " ").replace(".", " ").split()[:-2])}:')
                        print(f'Людей выше Вас по рейтингу с приоритетом 1 : {frst_n}')
                        print(f'Людей выше Вас по рейтингу : {all_n}')
                        print('')
                        print('')
                        break
    sleep(999_999_999)

