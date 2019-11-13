''''''


ones = {
    0: '', 1: 'jeden', 2: 'dwa', 3: 'trzy', 4: 'cztery', 5: 'pięć', 6: 'sześć',
    7: 'siedem', 8: 'osiem', 9: 'dziewięć', 10: 'dziesięć', 11: 'jedenaście',
    12: 'dwanaście', 13: 'trzynaście', 14: 'czternaście', 15: 'piętnaście',
    16: 'szesnaście', 17: 'siedemnaście', 18: 'osiemnaście',
    19: 'dziewiętnaście'}
tens = {
    2: 'dwadzieścia', 3: 'trzydzieści', 4: 'czterdzieści', 5: 'pięćdziesiąt',
    6: 'sześćdziesiąt', 7: 'siedemdziesiąt', 8: 'osiemdziesiąt',
    9: 'dziewięćdziesiąt'}
hundreds = {
    1: 'sto', 2: 'dwieście', 3: 'trzysta', 4: 'czterysta', 5: 'pięćset',
    6: 'sześćset', 7: 'siedemset', 8: 'osiemset', 9: 'dziewięćset'}
illions = {
    1: 'tysięcy', 2: 'milion', 3: 'miliard', 4: 'bilion', 5: 'biliard',
    6: 'tryliard', 7: 'kwintylion', 8: 'sextylion', 9: 'septylion',
    10: 'oktylion', 11: 'nonilion', 12: 'decylion'}

def say_number(i):
    """
    Convert an integer in to it's word representation.

    say_number(i: integer) -> string
    """
    if i < 0:
        return _join('negative', _say_number_pos(-i))
    if i == 0:
        return 'zero'
    return _say_number_pos(i)

def _say_number_pos(i):
    if i < 20:
        return ones[i]
    if i < 100:
        return _join(tens[get_digit(i, 1)], ones[get_digit(i, 0)])
    if i < 1000:
        if (get_digit(i, 1)) < 1:
            return _join(hundreds[get_digit(i, 2)], ones[get_digit(i, 0)])
        elif (get_digit(i, 1) < 2):
            return _join(hundreds[get_digit(i, 2)], ones[i % 100])
        else:
            return _join(hundreds[get_digit(i, 2)], tens[get_digit(i, 1)], ones[get_digit(i, 0)])
    if (i >= 1000 and i < 1000000):
        for illions_number, illions_name in illions.items():
            if i < 1000 ** (illions_number + 1):
                break
        if ((i // 1000) == 1):
            illions_name = 'tysiąc'
            return _divide(i, 1000 ** illions_number, illions_name)
        elif (get_digit(i, 3) > 1 and get_digit(i, 3) < 5):
            illions_name = 'tysiące'
            return _divide(i, 1000 ** illions_number, illions_name)
        else:
            illions_name = 'tysięcy'
            return _divide(i, 1000 ** illions_number, illions_name)
    if i >= 1000000:
        for illions_number, illions_name in illions.items():
            if i < 1000 ** (illions_number + 1):
                break
        if ((i // 1000 ** illions_number) == 1):
            return _divide(i, 1000 ** illions_number, illions_name)
        elif (i / 1000 ** illions_number > 5 and i / 1000 ** illions_number <= 19):
            illions_name = illions_name + 'ów'
            return _divide(i, 1000 ** illions_number, illions_name)
        elif (get_last_of_first_3_digits(i, illions_number) >= 2 and get_last_of_first_3_digits(i, illions_number) < 5):
            illions_name = illions_name + 'y'
            return _divide(i, 1000 ** illions_number, illions_name)
        else:
            illions_name = illions_name + 'ów'
            return _divide(i, 1000 ** illions_number, illions_name)


def get_last_of_first_3_digits(i, illions_number):
    return get_digit(i / (1000 ** illions_number), 0)


def _divide(dividend, divisor, magnitude):
    return _join(
        _say_number_pos(dividend // divisor),
        magnitude,
        _say_number_pos(dividend % divisor),
    )

def get_digit(number, n):
    return number // 10 ** n % 10

def _join(*args):
    return ' '.join(filter(bool, args))


