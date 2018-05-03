print('''3 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o 
rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes o maior que o 
estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa 
de R$ 4, 00 por quilo excedente João precisa que você faça um programa que leia a variável peso 
(peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável 
multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteudo ZERO''')

peso = float(input('Informe o Peso de Peixes: '))

if peso > 50.00:
	excesso = peso - 50.00
	multa = excesso * 4.00
	print('Você excedeu o peso em {:.2f}'.format(excesso))
	print('Terá que pagar multa no valor de {:.2f}'.format(multa))
else:
	excesso = 0
	multa = 0
	print('Você não excedeu o Peso, Parabéns!!!')