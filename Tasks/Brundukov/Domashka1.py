import time
# pip install colorama
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
ManyMan=0 
def tManyMan():
    print(Back.CYAN)
    global ManyMan
    ManyMan=decimal.Decimal(input("Введите сумму вклада:\n "))
    if ManyMan <= 1000:
        print(Back.RED)
        print('Денег для открытия вклада недостаточно!')
        return tManyMan()

def tTimeMan():
    print(Back.GREEN)
    global BAKS_PICS
    timer=int(input('Введите срок вклада(3--12% мес/процент,    6--11% мес/процент,    12--10% мес/процент,    24--9% мес/процент.):\n МЕС.--'))
    if timer !=3 and timer !=6 and timer != 12 and timer !=24:
        print("Вы вели не правильный срок вклада!\nПОВТОРИТЕ ВВОД!!")
        return tTimeMan()
    if timer==3:
        ocent1=12
    elif timer ==6:
        ocent1=11
    elif timer==12:
        ocent1=10
    elif timer==24:
        ocent1=9
    n=(ManyMan/100)*ocent1
    sum=ManyMan+n
    print(Back.MAGENTA)
    print("////ОЖИДАЙТЕ..ИДЕТ ПОДСЧЕТ СРЕДСТВ////")
    print(BAKS_PICS)
    time.sleep(4)
    print(Back.WHITE)
    print(Fore.BLUE)
    print('ВАША СУММА НА СЧЕТЕ ПО ВКЛАДУ НА КОНЕЦ СРОКА---------------------------------------------------------------------------------------',sum)
    
vvod_dan()
tManyMan()
tTimeMan()

