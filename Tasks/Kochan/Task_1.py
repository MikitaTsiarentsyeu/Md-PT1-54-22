import decimal


def amount(func):
    def wrapper(*args, **kwargs):
        print('Please enter deposit amount required (USD)')
        x = func(*args, **kwargs)
        return x

    return wrapper


def term(func):
    def wrapper(*args, **kwargs):
        print('Please enter deposit term required (months)')
        x = func(*args, **kwargs)
        return x

    return wrapper


def interest(func):
    def wrapper(*args, **kwargs):
        print('Please enter deposit interest rate (%)')
        x = func(*args, **kwargs)
        return x

    return wrapper


def decim():
    y = input()
    try:
        y = decimal.Decimal(y)
        return y
    except:
        print('The entered figure isn\'t correct, please try once more.')
        return decim()


def capit(a, b, c):
    cap = input('Do you want capitalization (please enter "yes" or "no")?  ')
    cap = cap.lower()
    if cap == 'yes':
        revenue = a * (1 + c / 100 / 12) ** (b * 12) - a
        print(f'If you put {a} USD for {b} months and bank interest rate is {c} % '
              f'per year you will get {revenue.quantize(decimal.Decimal("0.01"))} USD.')

    elif cap == 'no':
        revenue = a * b * c / 12 / 100

        print(f'If you put {a} USD for {b} months and bank interest rate is {c} % '
              f'per year you will get {revenue.quantize(decimal.Decimal("0.01"))} USD.')
    else:
        print('You haven\'t choose "yes" or "no", please try again.')
        capit(a, b, c)


a, b, c = amount(decim), term(decim), interest(decim)

a, b, c = a(), b(), c()

capit(a, b, c)
