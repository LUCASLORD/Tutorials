print('''5 - Faça um programa que peça um inteiro positivo e o mostre inventido Ex: 1234 gera 4321''')

num = int(input('Número: '))
inverso = 0
while num > 0:
	inverso *= 10
	inverso += num % 10
	num //= 10
print(inverso)

#dentro do while teremos inverso multiplicando 10
#inverso somando com o resto de num % 10
#num dividido por 10