print('''1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
seja inválido e continue pedindo até que o usuário informe um valor válido''')

n = 11

while n !=0 and n > 10:
	n = int(input('Informe uma nota:'))
	if n!=0 and n > 10:
		print('Nota inválida')
	else:
		print('Notava Válida encerrando')