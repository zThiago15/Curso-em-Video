celsius = float(input('\033[1;34mInforme uma temperatura em °C: '))
f = 1.8 * celsius + 32
k = celsius + 273.15
print(f'\033[34mA temperatura \033[33m{celsius}°C \033[34mem Fahrenheit corresponde à \033[33m{f:.2f}°F')
print(f'\033[34mE em Kelvin corresponde à \033[33m{k:.2f}°K')