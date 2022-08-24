################################################################################################################
# Реализовать:
# 1.текстовый вывод текущего времени
# 2.текстовый вывод времени, введённого c консоли (пользователь должен вводить данные в формате hh:mm).
# Дать пользователю возможность выбрать режим работы программы, время выводить числительными на русском языке.
#
# Для получения текущего времени использовать модуль datetime.
#
# min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
# min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
# min == 30: половина такого-то (15:30 - половина четвёртого)
# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
# min >= 45 без min такого-то (08:54 - без шести минут девять)
################################################################################################################

import json, os
from datetime import datetime
from msvcrt import getch


class EnTimeLenError(Exception):
    """Length error of entered time"""

    def __init__(self, text):
        self.txt = text


class HoursError(Exception):
    """Hours interval error, not in 0-24 hours"""

    def __init__(self, text):
        self.txt = text


class MinsError(Exception):
    """Mins interval error, not in 0-60 mins"""

    def __init__(self, text):
        self.txt = text


class HoursAndMinsError(Exception):
    """Time interval error, more than 24:00"""

    def __init__(self, text):
        self.txt = text


class SeparatorError(Exception):
    """Separator error between hours and mins"""

    def __init__(self, text):
        self.txt = text


def EnTime_validation(EnTime):
    """Checking entered time on errors
    
    Keyword arguments:
    EnTime - time entered by user
    """
    try:
        hh, separator, mm = EnTime[0:2], EnTime[2], EnTime[3:5]
        if len(EnTime) != 5:
            raise EnTimeLenError("")
        if int(hh) not in range(0, 25):
            raise HoursError("")
        if int(mm) not in range(0, 60):
            raise MinsError("")
        if int(hh) == 24 and int(mm) != 0:
            raise HoursAndMinsError("")
        if separator != ":":
            raise SeparatorError("")
        return int(hh), int(mm)

    except EnTimeLenError:
        print("Ошибка количества символов времени. Попробуйте еще раз.")
        return any_time()
    except HoursError:
        print("Ошибка: в сутках всего 24 часа. Попробуйте еще раз.")
        return any_time()
    except MinsError:
        print("Ошибка: в одном часе всего 60 минут. Попробуйте еще раз.")
        return any_time()
    except HoursAndMinsError:
        print("Ошибка: в сутках всего 24:00 часа. Попробуйте еще раз.")
        return any_time()
    except SeparatorError:
        print(f"Ошибка ввода сепаратора времени: '{separator}' вместо ':'. Попробуйте еще раз.")
        return any_time()
    except ValueError:
        print("Ошибка: часы и минуты должны быть записаны цифрами от 0 до 60")
        return any_time()
    except:
        print("Ошибка: незнакомое времяисчисление. Попробуйте еще раз")
        return any_time()


def program_exit(func):
    """Request for exit or continue"""

    def wrapper():
        flag = True
        while flag:
            func()
            print("Для выхода нажми ESC или любую кнопку, чтобы продолжить:")
            key = ord(getch())
            flag = True if key != 27 else False
        print("Спасибо на использование приложения.")

    return wrapper


def any_time():
    """Request for user time input"""
    EnTime = input("Введите время в формате hh:mm :\n")
    hours, mins = EnTime_validation(EnTime)
    hours = hours - 12 if hours >= 12 else hours
    return hours, mins


def current_time():
    """Request for current time"""
    cur_time = datetime.now()
    hours = int(cur_time.hour)
    hours = hours - 12 if hours > 12 else hours
    mins = int(cur_time.minute)
    return hours, mins


def time_working_mode(current_time, any_time):
    """Request for program working mode - current time or user time"""
    os.system('cls')
    time_choice = input(
        "Вывести текущее время ('да') или указать время вручную (любая кнопка):\n"
    )
    if time_choice == "да" or time_choice == "lf":
        hours, mins = current_time()
    else:
        hours, mins = any_time()
    return hours, mins


@program_exit
def time_2_words():
    """Time dictionary output handler
    
    Keyword arguments:
    hours - current hours or user entered hours
    mins - current mins of hour or user entered mins
    """
    os.system('cls')
    hours, mins = time_working_mode(current_time, any_time)

    with open(f"{os.path.dirname(__file__)}\cases_of_numbers.json",
              "r") as file:
        dct = json.load(file)

    dhn = dct["Hours"]["Nominative"]  # dhn - dct_hours_nominative
    dhg = dct["Hours"]["Genetive"]  # dhg - dct_hours_genetive
    dmn = dct["Minutes"]["Nominative"]  # dmn - dct_mins_nominative
    dmg = dct["Minutes"]["Genetive"]  # dmg - dct_mins_genetive

    if mins == 0:
        if hours in [1]:
            time_in_words = (f"один {dhn[str(hours)]} ровно")
        elif hours in [2, 3, 4]:
            time_in_words = (f"{dhn[str(hours)]} часа ровно")
        else:
            time_in_words = (f"{dhn[str(hours)]} часов ровно")

    if mins in range(1, 30) or mins in range(31, 45):
        if mins in [1, 21, 31]:
            time_in_words = (f"{dmn[str(mins)]} минута {dhg[str(hours+1)]}")
        elif mins in [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44]:
            time_in_words = (f"{dmn[str(mins)]} минуты {dhg[str(hours+1)]}")
        else:
            time_in_words = (f"{dmn[str(mins)]} минут {dhg[str(hours+1)]}")

    if mins == 30:
        time_in_words = (f"половина {dhg[str(hours+1)]}")

    if mins in range(45, 60):
        if mins in [59]:
            time_in_words = (
                f"без {dmg[str(60-mins)]} минуты {dhn[str(hours+1)]}")
        else:
            time_in_words = (
                f"без {dmg[str(60-mins)]} минут {dhn[str(hours+1)]}")
    print(f"Время: {time_in_words}.")


if __name__ == '__main__':
    time_2_words()
