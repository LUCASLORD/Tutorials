print('''5 - Solicite o preço de uma mercadoria e o percentual de desconto. 
Exiba o valor do desconto e o preço a pagar''')

preço = float(input('Informe o preço da mercadoria: '))
desconto = float(input('Informe o percentual de desconto: '))

preçopagar = preço - ((preço * desconto) /100)

print('A mercadoria teve um desconto de {}'.format(preço))
print('O preço a pagar é {}'.format(preçopagar))
