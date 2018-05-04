print('''1 - Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. 
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular''')

n = int(input('Informe um Número: '))
i = 0

while i < n:
	if (i * (i+1) * (i+2)) == n:
		print('O Número é triangular')
		break
	elif i == n-1:
		print('O número não é triangular')
	else:
		i = i + 1