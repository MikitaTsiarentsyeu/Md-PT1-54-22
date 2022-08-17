# {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
# 4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
# 9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
# 6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
# 7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

# data structure is given, you need to give the user the ability to search by phone number
# output in case of match - "{firstname} {lastname} from {city}, {state}"
# in case of mismatch - "the number was not found"

# provide validation on the length of the entered string and on its characters (should be numbers)

from os import system
from msvcrt import getch

dct = {
    9103976271: [("Reina", "Meinhard"), ("Memphis", "Tennessee")],
    4199392609: [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
    9099459979: [("Ermes", "Angela"), ("Dallas", "Texas")],
    6123479367: [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
    7548993768: [("Margarete", "Quintin"), ("Raleigh", "North Carolina")]
}


class phone_number_len_error(Exception):
    """Private exception if the number length not equal 10 digits"""

    def __init__(self, text):
        self.txt = text


def phone_number_verification():
    """Phone number verification.
    
    Function checks entered phone number on number length, which should be 10 digits,
    and checks if the number is correct without any symbols and alphas.
    """

    try:
        phone_number = input("Please, enter the telephone number:\n")
        if int(phone_number) <= 0:
            raise Exception
        if len(phone_number) != 10:
            raise phone_number_len_error(
                "Phone number should be 10 digits. Try again, please")
        return phone_number
    except phone_number_len_error:
        print("Phone number should be 10 digits. Try again, please.")
        return phone_number_verification()
    except:
        print("Entered phone number is incorrect. Try again, please.")
        return phone_number_verification()


def program_exit(func):
    """Request for exit or continue"""

    def wrapper(arg1):
        flag = True
        while flag:
            func(arg1)
            print("Press ESC for exit or any button to start new request:")
            key = ord(getch())
            flag = True if key != 27 else False
        print("ESCAPE\nThank you for using this app.")

    return wrapper


@program_exit
def user_request_from_dictionary(dct):
    """Request to predefined dictionary on entered phone number
    
    Keyword arguments:
    dct - predefined dictionary of datas: {phone_number: [("Firstname", "Lastname"), ("City", "State")]}
    """
    pnv = int(phone_number_verification())
    if pnv in dct:
        system('cls')
        print(
            f"{pnv}: {dct[pnv][0][0]} {dct[pnv][0][1]} from {dct[pnv][1][0]}, {dct[pnv][1][1]}"
        )
    else:
        system('cls')
        print(f"The number {pnv} was not found.")


if __name__ == '__main__':
    system('cls')
    user_request_from_dictionary(dct)
