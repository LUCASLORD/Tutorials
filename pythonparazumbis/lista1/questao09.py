print('''9 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro 
custa R$60,00 por dia e R$0,15 por km rodado.''')

qtdkm = int(input('Informe a Quantidade de km percorridos: '))
qtddias = int(input('Informe a quantidade de dias: '))

preçopagar = (60 * qtddias) + (qtdkm * 0.15)

print('Preço a pagar total pelo aluguel do veiculo {:.2f}'.format(preçopagar))