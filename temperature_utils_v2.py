from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    
    celsius_temp = (fahrenheit_temp - 32) * 5 / 9
    return round(celsius_temp, 2)


def convert_to_fahrenheit(celsius_temp: float) -> float:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    
    fahrenheit_temp = celsius_temp * 9 / 5 + 32
    return round(fahrenheit_temp, 2)


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    
    if input_unit_of_measurement == 'f':
        f = []
        for i in temperatures:
            f.append((i, round(((i-32)*5/9), 2)))
        return tuple(f)

    elif input_unit_of_measurement == 'c':
        c = []
        for j in temperatures:
            c.append((j, round(j*9/5+32, 2)))
        return tuple(c)

    elif input_unit_of_measurement == 'k':
        kel = []
        for k in temperatures:
            kel.append((k, round((k)+273.15)))
        return tuple(kel)

    elif input_unit_of_measurement != 'f' or input_unit_of_measurement != 'c'or input_unit_of_measurement != 'k':
        return ()

    f = temperature_tuple((32, 68, 100, 104), 'f')
    print(f)

    c = temperature_tuple((-17.7778, 0, 100), 'c')
    print(c)

    kel = temperature_tuple((-17.7778, 0, 100), 'k')
    print(f)

    f = temperature_tuple((1, 2, 3), 'a')
    print(f)
