from math import ceil
def convert_temp(reading, users_choice):
    value, unit = reading.split('°')
    value = int(value.strip())


    if users_choice == 'C':
        if unit == 'C':
            return f'{value}°C.'
        else:
            celsius_temp = ceil((value - 32) * 5 / 9)
            return f'{celsius_temp}°C.'

    if users_choice == 'F':
        if unit == 'F':
            return f'{value}°F.'
        else:
            fahr_temp = ceil(value * 9/5 + 32)
            return f'{fahr_temp}°F.'

    else:
        return "Invalid choice."

