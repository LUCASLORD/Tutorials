print('''\n3 - Escreva um programa que leia a quantidade de dias,horas, 
minutos e segundos do usuário. Cálcule o total em segundos\n''')

dias = int(input('Informe a quantidade de dias '))
horas = int(input('Informe a quantidade de horas '))
minutos = int(input('Informe a quantidade de minutos '))
segundos = int(input('Informe a quantidade de segundos '))

totalsegundos = segundos+((minutos+((horas+(dias*24))*60))*60)

print('''\n{} dias, {} horas, {} minutos e {} segundos,
equivalem a {} segundos no total'''.format(dias,horas,minutos,segundos,totalsegundos))