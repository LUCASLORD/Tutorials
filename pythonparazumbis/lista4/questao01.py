print('''1 - Sortei 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funçoes max e min.''')
from random import randint

lista = []
i = 0 
maior = 0 
menor = 100

while i < 10:
	lista.append(randint(1,100))
	if lista[i] > maior:
		maior = lista[i]
	elif lista[i] < menor:
		menor = lista[i]
	i += 1

print(lista)
print("O Menor Valor foi {}".format(menor))
print("O Maior Valor Foi {}".format(maior))