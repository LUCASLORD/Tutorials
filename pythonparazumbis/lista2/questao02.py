print('''Determine se um ano é bissexto
Bissexto:  1980, 1984, 1988, 1992, 1996 e 2000.
 1900 não foi bissexto, mas 1600 foi \n''')

ano = int(input('Informe o Ano Desejado: '))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0 :
	print('o ano {} é bissexto'.format(ano))
else:
	print('o ano {} não é bissexto'.format(ano))
