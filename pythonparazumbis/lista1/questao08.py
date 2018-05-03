print('''8 - Faça agora o contrário, de Fahrenheit para Celsius''')

Fahrenheit = float(input('Informe a Temperatura em Fahrenheit: '))

celsius = ((Fahrenheit - 32) * 5) / 9

print('{} graus Fahrenheit equivalem à {} graus celsius'.format(Fahrenheit,celsius))