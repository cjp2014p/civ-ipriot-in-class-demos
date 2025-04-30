# def convert_temp(temp, unit):
#     if unit.lower() == 'f':
#         converted_temp = (temp - 32) * 5 / 9
#     else:
#         converted_temp = temp * 9 / 5 + 32
#     return converted_temp
#
# t = convert_temp(42, 'c')
# print(t)

# alternative advanced version
def convert_temp(temp, unit):
    if unit.lower() not in ['c', 'f']:
        raise ValueError("Invalid Unit")
    if unit.lower() == 'f':
        converted_temp = (temp - 32) * 5 / 9
    else:
        converted_temp = temp * 9 / 5 + 32
    return converted_temp

# commented out next block for use with my_program test
# try:
#     t = convert_temp(42, 'k')
# except ValueError:
#     print("please put a valid unit")

print("__name__", __name__)

if __name__ == "__main__":
    print("Yippie I am a script now!")
else:
    print("I am a module now")