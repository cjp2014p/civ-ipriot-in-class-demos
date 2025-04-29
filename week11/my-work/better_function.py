def convert_temp(temp, unit):
    if unit.lower() == 'f':
        converted_temp = (temp - 32) * 5 / 9
    else:
        converted_temp = temp * 9 / 5 + 32
    return converted_temp

t = convert_temp(42, 'c')
print(t)