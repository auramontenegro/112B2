# Function to convert from Celsius to Fahrenheit

def fahrenheit(celsius):
    """Converts degrees celsius to fahrenheit"""
    return ((9 * celsius) / 5) + 32


def fahrenheit_list(celsius_lst):
    """converts a list of temperatures in degrees celsius to fahrenheit"""
    fahrenheit_lst = []
    for celsius_temp in celsius_lst:
        fahrenheit_temp = fahrenheit(celsius_temp)
        fahrenheit_lst = fahrenheit_lst + [fahrenheit_temp]
    return fahrenheit_lst

