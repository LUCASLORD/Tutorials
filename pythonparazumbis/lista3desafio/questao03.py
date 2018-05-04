print('''3 - Verifique se um inteiro positivo n é primo''')

n = int(input('Informe um número: '))
i = 1
div = 0

while i <= n:
	if n % i == 0:
		div = div + 1
	i = i + 1
if div > 2:
	print('Não é Primo')
else:
	print('É primo')