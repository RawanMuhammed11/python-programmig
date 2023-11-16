
def temp(fahrenheit):
    celsius = (fahrenheit -32) * 5/9
    kelvin = celsius + 273.15
    return celsius,kelvin
fahrenheit=float(input("enter the fahrenheit temperature:"))
celsius, kelvin = temp(fahrenheit)
print(f"{celsius:.2f} degrees Celsius")
print(f"{kelvin:.2f} Kelvin")