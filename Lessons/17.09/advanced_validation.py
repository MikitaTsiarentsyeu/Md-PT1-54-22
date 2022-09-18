
def validate_time(value):
    try:
        if len(value) != 5 or not ':' in value:
            raise RuntimeError("your value was in incorrect format")
    
        values = value.split(':')
        is_hours = True
        for splited_value in values:
            validate_hours_and_minutes(splited_value, is_hours)
            if is_hours:
                is_hours = not is_hours
    
    except RuntimeError as er:
        return str(er)
    except ValueError:
        return "please use digits to specify the hours and minutes values"

def validate_hours_and_minutes(value, is_hours):
    value = int(value)
    if value < 0:
        raise RuntimeError("The hours and minutes values must be higher than 0")
    if is_hours and value > 23:
        raise RuntimeError("The hours value must be lower than 24")
    if not is_hours and value > 59:
        raise RuntimeError("The minutes value must be lower than 60")

while True:
    time = input("Please enter your value in format hh:mm\n")
    validation_res = validate_time(time)
    if validation_res:
        print(validation_res)
    else:
        break

print("the main logic")