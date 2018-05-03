print('''5 - Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides''')

a = int(input('Informe Um Número: '))
b = int(input('Informe Outro Número: '))
while (b != 0):
    r = a % b
    a = b
    b = r
    
print(a)