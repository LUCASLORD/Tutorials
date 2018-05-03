print('''4 - Faça um programa que leia três números e mostre o maior deles''')

n1 = int(input('Informe Primeiro Número: '))
n2 = int(input('Informe Segundo Número: '))
n3 = int(input('Informe Terceiro Número: '))

if n1 > n2 and n1 > n3:
	print('O Maior Número é {}'.format(n1))
elif n2 > n1 and n2 > n3:
	print('O Maior Número é {}'.format(n2))
else:
	print('O Maior Número é {}'.format(n3))
