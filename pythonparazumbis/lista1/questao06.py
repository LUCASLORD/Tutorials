print('''6 - Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer 
e a velocidade média esperada para a viagem.''')

distância = float(input('Informe a distância a ser percorrida: '))
velocidade = float(input('Informe a velocidade Média: '))

tempo = (distância / velocidade)

print('O tempo estimado é de {} hora(s) e {:.0f} minuto(s)'.format(int(tempo),100*(tempo-int(tempo))))
