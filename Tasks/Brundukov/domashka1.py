
import time
# pip install colorama(Для установки библиотеки в терминале)
from colorama import init 
from colorama import Fore,Back,Style
import decimal
BAKS_PICS=("  ++|++\n +  |  +\n  + |\n    +\n    |  +\n +  |  +\n  ++|++\n////ОЖИДАЙТЕ..ИДЕТ ПОДСЧЕТ СРЕДСТВ////")
  
def vvod_dan():
    print(Style.DIM)
    print(Back.YELLOW)
    print('''Вы захотели положить деньги под процент???! 
    \tВЫ выбрали лучшее место для этого!!
    Только наш банк продоставлят самый высокий процент по стране!!
    Пожалуйста введите сумму вклада(не менее 1000$)
    А так же срок вклада (3 мес.;6 мес.;12 мес.; 24 мес.)''' )
    print()

def tManyMan():
    print(Back.CYAN)
    global ManyMan
    ManyMan=decimal.Decimal(input("Введите сумму вклада:\n "))
    if ManyMan <= 1000:
        print(Back.RED)
        print('ваша сумма вклада слишком мала,ознакомьтесь с порогами входа!Повторите ввод!')
        return tManyMan()

def tTimeMan():
    global BAKS_PICS
    time.sleep(2)
    print(Back.GREEN)
    timer=decimal.Decimal(input('Введите срок вклада(3--15% мес/процент,    6--14% мес/процент,    12--13% мес/процент,    24--12% мес/процент.):\n МЕС.--'))
    if timer !=3 and timer !=6 and timer != 12 and timer !=24:
        print(Back.RED)
        print("Вы вели не правильный срок вклада!\nПОВТОРИТЕ ВВОД!!")
        return tTimeMan()
    if timer==3:
        ocent1=15
    elif timer ==6:
        ocent1=14
    elif timer==12:
        ocent1=13
    elif timer==24:
        ocent1=12
    sum=((ManyMan/100)*ocent1)+ManyMan
    print(Back.MAGENTA)
    print("////ОЖИДАЙТЕ..ИДЕТ ПОДСЧЕТ СРЕДСТВ////")
    print(BAKS_PICS)
    time.sleep(4)
    print(Back.MAGENTA)
    print(Fore.BLACK)
    print('ВАША СУММА НА СЧЕТЕ ПО ВКЛАДУ НА КОНЕЦ СРОКА---------------------------------------------------------------------------------------',sum)
    
vvod_dan()
tManyMan()
tTimeMan()