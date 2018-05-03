print('''4 - Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salário e a porcentagem do aumento. 
Exiba o valor do aumento e do novo solário.\n''')

salário = float(input('Informe o salário: '))
aumento = float(input('Informe o aumento em %: '))

novosalário = salário + ((aumento * salário)/100)

print('\nO salário {}, teve {} de aumento'.format(salário,aumento))
print('Salário final {}'.format(novosalário))