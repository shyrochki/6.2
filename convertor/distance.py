from math import ceil
def convert_dist(distance, ft_or_m):
    distance = distance.strip('"')

    # Extract the numeric value and the unit
    value_str, unit = distance.split(' ', 1)
    value = int(value_str)

    if ft_or_m == 'ft':
        if unit == 'ft':
            return f'{value}ft'
        else:
            ft_distance = ceil(value/0.3089)
            return f' {ft_distance}ft'
    elif ft_or_m == 'm':
        if unit == 'm':
            return f'{value}m'
        else:
            m_distance = ceil(value * 0.3089)
            return f' {m_distance}m'

    else:
        return "Invalid choice."

