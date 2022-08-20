# The user sets the deposit values:
# initial amount (for example, 20000)
# term in years (for example, 5))
# annual percentage (for example, 15)

# It is also worth asking the user to enable monthly capitalization.

# It is necessary to calculate the amount on the account at the end of the
# specified period and issue a response to the user.

from decimal import Decimal
from os import system

system('cls')


class MyError(Exception):
    def __init__(self, text):
        self.txt = text


def decimalization(txt):
    """Transform inputed string to Decimal"""
    try:
        x_in_dec = Decimal(input(txt))
        if x_in_dec <= 0:
            raise MyError("The number must be greater than 0. Try again")
        return x_in_dec
    except MyError:
        print("The number must be greater than 0. Try again")
        return decimalization(txt)
    except:
        print("The number is not correct. Try again")
        return decimalization(txt)


def capitalization():
    """Users choice of capitalization - YES or NO"""
    try:
        capitalization_choice_string = input(
            "Include monthly capitalization (y = YES, other different = NO):\n"
        )
        if capitalization_choice_string == "y":
            capitalization_choice = True
        else:
            capitalization_choice = False
        return capitalization_choice
    except:
        print("Inputed data is wrong. Try again")
        return capitalization()


def total_depozit(deposit, deposit_term, annual_percentage):
    """Total depozit at the end of deposit term with capitalization and without

    Keyword arguments:
    deposit - USD deposit at the beginning of the term;
    deposit_term - time period of deposit in years;
    annual_percentage - deposit percentage in %

    """
    try:
        if capitalization():
            cap = "with"
            deposit_term_months = deposit_term * 12
            total = deposit
            while deposit_term_months != 0:
                total = total + \
                    round(total * (annual_percentage / 12 / 100), 2)
                deposit_term_months -= 1
        else:
            cap = "without"
            total = deposit + deposit * \
                deposit_term * (annual_percentage / 100)
    except:
        print("Something goes wrong. Try again")

    system('cls')
    print(
        f"Total deposit at the end of the term is:\n{total} USD\nYour benefit from {deposit} USD per {deposit_term} years under {annual_percentage}% {cap} capitalization is:\n{total-deposit} USD")


if __name__ == '__main__':
    deposit = decimalization("Enter your deposit (USD):\n")
    deposit_term = decimalization("Enter your deposit term (years):\n")
    annual_percentage = decimalization("Enter your annual percentage (%):\n")
    total_depozit(deposit, deposit_term, annual_percentage)
