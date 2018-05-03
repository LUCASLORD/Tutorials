print('''10 - Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de 
vida um fumante perderá. Exiba o total de dias.''')

cigarrosdia = int(input('Informe a quantidade de cigarros fumados por dia: '))

anos = int(input('Informe a quantidade de anos que já fumou: '))

diasvida = (((((anos * 365) * cigarrosdia) * 10) / 60) / 24)

print('Você perdera {:.2f} dias de vida'.format(diasvida))