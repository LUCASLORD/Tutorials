print('''\n2 - Escreva um programa que leia um valor em metros
e o exiba convertido em milímetros.
''')
metros = float(input('Informe a metragem: '))

milímetros = ( metros * 100 ) * 10

print('\n{} metros equivale à {:.2f} milímetros'.format(metros, milímetros))