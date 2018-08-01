print('''2 - Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas''')

from random import randint

lista = []
i = 0
PAR = []
IMPAR = []

while i < 20:
	lista.append(randint(1, 100))
	if lista[i] % 2 == 0:
		PAR.append(lista[i])
	else:
		IMPAR.append(lista[i])
	i+= 1

print("Lista: {}".format(lista))
print("Pares: {}".format(PAR))
print("Impares: {}".format(IMPAR))