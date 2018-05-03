print('''4 - A sequência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,... 
Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, 
cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia um número inteiro 
calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F 3 = 2, etc''')

n = int(input('Informe a posição que quer saber de fibonacci: '))

fib = 2 
ant = 0
i = 0

while i < n:
	if i == 0 or i == 1:
		print(1)
	else:
		print(fib)
		fib = fib + (i - 1)
	i = i + 1

	