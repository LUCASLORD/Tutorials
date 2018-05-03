print('''7 - Converta uma temperatura digitada em Celsius para Fahrenheit. F=9*C/5 +32''')

celsius = float(input('Informe a Temperatura em Celsius: '))

fahrenheit = (9 * celsius) / 5 + 32

print('{} graus celsius equivalem à {} graus fahrenheit'.format(celsius, fahrenheit))
