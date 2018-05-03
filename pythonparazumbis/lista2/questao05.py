print('''5 - Faça um Programa que Leia 3 Números e mostre o maior e o menor deles.''')

n1 = int(input('Informe Primeiro Número: '))

maior = n1
menor = n1

n2 = int(input('Informe Segundo Número: '))

if n2 > maior:
	maior = n2
if n2 < menor:
	menor = n2
	
n3 = int(input('Informe Terceiro Número: '))

if n3 > maior:
	maior = n3
if n3 < menor:
	menor = n3
	
print('O Maior Número digitado foi {}'.format(maior))
print('O Menor Número digitado foi {}'.format(menor))
