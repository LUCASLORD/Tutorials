print('''3 - Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores''')

from random import randint
vetorUm = []
vetorDois = []
vetorTres = []
i = 0 

while i < 10:
	vetorUm.append(randint(1,100))
	vetorDois.append(randint(1,100))
	vetorTres.append(vetorUm[i])
	vetorTres.append(vetorDois[i])
	i += 1

print("\n")
print("Lista Um: {}".format(vetorUm))
print("Lista Dois: {}".format(vetorDois))
print("Listas Intercaladas \n {}".format(vetorTres))