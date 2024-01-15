
import random
from threading import Timer
f = open(r'russian.txt').readlines()
letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п",
           "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
zapret = ['ь', 'ъ']
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]


def proverka(choser):
    if choser[0] in zapret and choser[1] in vse_gls:
        return False
    if choser[1] in zapret and choser[0] in vse_gls:
        return False
    return True


def create():
    while True:
        choser = ''.join(random.choices(letters, k=2))
        if proverka(choser):
            return choser


def task(message):
    # report the custom message

    print(message)
    raise NameError('HiThere')
    exit()


def check_input(choser, f):
    while True:
        inn = input(f'{choser}:-')
        if f'{inn}\n' in f:

            break
        else:
            print('плох')
    return True


print('добро пожаловать')

while True:
    choser = create()
    # таймер запускается на 5 секунд и паралельно запускается check_input()
    timer = Timer(7, task, args=('Время кончилось',))
    timer.start()


    if check_input(choser, f):
        print('хор')
        timer.cancel()
    else:
        # рандом
        continue
