print('''4 - Dado um número inteiro positivo, determine a sua decomposição em fatores primos 
calculando também a multiplicidade de cada fator''')

num = int(input('Informe Número: '))
for i in range(2, num):
	while num % i == 0 :
		print(i)
		num = num / i

""" Nota: Teremos um range de 2 (menor primo) a N, faremos o teste da divisão observando o 
resto e levando em consideração a fatoração enquanto for possível ex: 8 / 2 da 2 com resto 4, 
depois 4 / 2 da 2 com resto 2 mostraremos a posição do I (fator) e depois o Num será O numero 
inicial dividido pelo fator onde observando o que foi explicado acima teremos 8 / 2 = 4, no 
próximo teste será 4 % 2 e assim sucessivamente"""