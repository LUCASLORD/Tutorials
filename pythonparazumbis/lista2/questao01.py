print('''1 - Faça um programa que peça os três lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. Indique, 
caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno/n''')

a = float(input('Informe o Primeiro Lado'))
b = float(input('Informe o Segundo Lado'))
c = float(input('Informe o Terceiro Lado'))

if a-b < c < a + b:
	print('os 3 lados informados podem formar um triângulo')
	if a==b==c:
		print('Triângulo equilátero 3 lados iguais')
	elif a==b or a==c or b==c:
		print('Triângulo isósceles 2 lados iguais')
	else:
		print('Triângulo escaleno 3 lados diferentes')
else:
	print('os 3 lados informados não podem formar um Triângulo')