# Function 1: Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# Function 2: Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# Function 3: Convert temperature based on unit
def convert_temperature(temperature, unit):
    if unit == 'C':
        return celsius_to_fahrenheit(temperature)
    elif unit == 'F':
        return fahrenheit_to_celsius(temperature)
    else:
        return "Invalid unit. Use 'C' or 'F'."