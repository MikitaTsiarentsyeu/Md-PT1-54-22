############################################################################
# 1. Подготовиться к чтению содержимого файла text.txt
# 2. Дать пользователю ввести с клавиатуры параметр "максимальное количество символов в строке", который должен быть больше 35
# 3. Отформатировать текст с учётом максимального количества символов, при этом если слово целиком не умещается в строке, оно должно быть перенесено на следующую, а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
# 4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
# (модуль textwrap использовать нельзя)
############################################################################

import tkinter
from tkinter import filedialog
from os import system
from msvcrt import getch


def program_exit(func):
    """Request for exit or continue"""

    def wrapper():
        flag = True
        while flag:
            func()
            print("Press ESC for exit or any key for continue:")
            key = ord(getch())
            flag = True if key != 27 else False
        print("Thank you for using app.")

    return wrapper


def line_handler(txt):
    """Text clearing from double-spaces and adding line break at the end of the text file"""

    while "  " in txt:
        txt = str(txt).replace("  ", " ")
    if txt[-1] != "\n":
        txt = txt + "\n"
    return txt


def file_to_format():
    """Choosing file to format"""

    root = tkinter.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    try:
        print(input("Please select the file to format the text (press ENTER for continue): "))
        file_path_open = filedialog.askopenfilename()
        if not file_path_open:
            raise Exception
        else:
            print(f"File to format: {file_path_open}")
        return file_path_open
    except:
        print("File to format were not chosen. Try again please.")
        return file_to_format()


def path_to_save():
    """Choosing path to save"""

    root = tkinter.Tk()
    root.withdraw()
    try:
        print(input("Choose a path to save the formatted text (press ENTER for continue): "))
        file_path_save = filedialog.asksaveasfilename()
        if not file_path_save:
            raise Exception
        else:
            print(f"Path to save formatted text: {file_path_save}")
        return file_path_save
    except:
        print("Path to save the formatted text were not chosen. Try again please.")
        return path_to_save()


class TextWidthError(Exception):
    """Text width error for max number of chars for text formatting (more than 35 chars)"""

    def __init__(self, text):
        self.txt = text


def text_width_validation(text_width):
    """Text width validation on more than 35 char length"""

    try:
        if int(text_width) < 35:
            raise TextWidthError("")
        else:
            return text_width
    except TextWidthError:
        print("The number of chars for text formatting must be equal or greater than 35 chars. Try again please.")
        return text_width_request()
    except ValueError:
        print("The number of chars for text formatting must be digital. Try again please.")
        return text_width_request()
    except:
        print("Something goes wrong. Try again please.")
        return text_width_request()


def text_width_request():
    """Request for text width formatting"""

    text_width = input("Enter max number of chars for text formatting (more than 35 chars):\n")
    text_width = text_width_validation(text_width)
    return int(text_width)


def space_inserter(short_line, text_width):
    """Space inserter between words for line extension to predefined width"""

    line_in_words = str(short_line).split()
    line_in_words_len = len(line_in_words)
    number_of_spaces = text_width - len(short_line) + (line_in_words_len - 1)
    if short_line[-1] == "\n":
        short_line = short_line.strip()
        return short_line
    elif line_in_words_len > 1:
        glue = " "
        spaces_base = glue * (number_of_spaces // (line_in_words_len - 1))
        spaces_corr = number_of_spaces % (line_in_words_len - 1)
        short_line = spaces_base.join(line_in_words)
        short_line = str(short_line).replace(spaces_base, spaces_base + glue, spaces_corr)
        return short_line


@program_exit
def text_leveler():
    """Text leveler"""

    system("cls")
    file_path_open = file_to_format()
    file_path_save = path_to_save()
    text_width = text_width_request()
    with open(file_path_save, "w", encoding="utf-8") as outf:
        with open(file_path_open, "r", encoding="utf-8") as inf:
            for line in inf:
                line = line_handler(line)
                start_point = 0
                end_point = start_point + text_width + 1
                short_line = True
                xchar = ""
                while line:
                    short_line = line[start_point:end_point]
                    xchar = short_line[-1]
                    if xchar == " ":
                        short_line = " ".join(short_line.split())
                    elif xchar not in [" ", "\n"]:
                        short_line = " ".join(short_line.split()[:-1])
                    line = line[len(short_line) + 1:]
                    short_line = space_inserter(short_line, text_width)
                    outf.writelines(short_line + "\n")
    print(f"Formatted text placed in file {file_path_save}")


if __name__ == '__main__':
    text_leveler()
