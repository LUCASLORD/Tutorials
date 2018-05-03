print('''7 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros 
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a 
quantidades de latas de tinta a serem compradas e o preço total. Obs.: somento são vendidos um número 
inteiro de latas.''')

metros = float(input('Informe o tamanho da área em m²: '))

if metros > 18 * 3:
	litros = metros / 3
	if litros % 18 > 0:
		qtdlata = litros // 18 + 1
		preco = qtdlata * 80
		print('Você precisará de {} latas, ao custo de R$ {}'.format(qtdlata,preco))
else:
	print('Você precisará de apenas Uma Lata ao custo de R$ 80,00')
	